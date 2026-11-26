from math import comb, pi

import numpy as np
from scipy.optimize import linprog


def parity_weights(copies, weights):
    even = np.zeros(weights.size + copies)
    odd = np.zeros_like(even)
    for charge in range(copies + 1):
        target = odd if charge % 2 else even
        target[charge:charge + weights.size] += (
            weights * comb(copies, charge) / (2 ** copies)
        )
    return even, odd


def reference_profile(width, copies):
    locations = np.arange(1, width + 2)
    weights = np.sin(pi * locations / (width + 2)) ** copies
    return weights / weights.sum()


def program(copies, weights):
    if copies == 1:
        return np.zeros(0)
    even, odd = parity_weights(copies, weights)
    constraints = np.zeros((weights.size + copies, copies - 1))
    for shift in range(1, copies):
        constraints[shift:shift + weights.size, shift - 1] = weights
    result = linprog(
        -np.ones(copies - 1),
        A_ub=constraints,
        b_ub=2 * np.minimum(even, odd),
        bounds=(0, None),
        method="highs",
    )
    assert result.success, result.message
    return result.x


def even_construction(copies, weights):
    even, odd = parity_weights(copies, weights)
    mask = odd > 0
    probability = min(1.0, np.min(even[mask] / odd[mask]))
    mass = np.zeros(copies - 1)
    for shift in range(1, copies, 2):
        mass[shift - 1] = probability * comb(copies, shift) / 2 ** (copies - 1)
    return mass


def verify_instrument(copies, weights, mass):
    width = weights.size - 1
    phase = 0.473
    reference = np.sqrt(weights) * np.exp(1j * phase * np.arange(width + 1))
    dimension = (width + 1) * (copies + 1)
    inputs = {sign: np.zeros(dimension, dtype=complex) for sign in (1, -1)}
    instruments = {
        (sign, shift): np.zeros((width + 1, dimension), dtype=complex)
        for sign in (1, -1)
        for shift, amount in enumerate(mass, 1)
        if amount > 0
    }
    reference_template = np.sqrt(weights)
    for total in range(width + copies + 1):
        even = np.zeros(dimension)
        odd = np.zeros(dimension)
        for charge in range(copies + 1):
            ref_charge = total - charge
            if 0 <= ref_charge <= width:
                target = odd if charge % 2 else even
                index = ref_charge * (copies + 1) + charge
                target[index] = reference_template[ref_charge] * np.sqrt(
                    comb(copies, charge) / (2 ** copies)
                )
        e_norm, o_norm = even @ even, odd @ odd
        for sign in (1, -1):
            inputs[sign] += np.exp(1j * phase * total) * (even + sign * odd)
        if min(e_norm, o_norm) == 0:
            continue
        for (sign, shift), matrix in instruments.items():
            output = total - shift
            if 0 <= output <= width:
                matrix[output] += (
                    np.sqrt(mass[shift - 1]) * reference_template[output] / 2
                ) * (even / e_norm + sign * odd / o_norm)
    effect = np.zeros((dimension, dimension), dtype=complex)
    for (sign, shift), matrix in instruments.items():
        effect += matrix.conj().T @ matrix
        assert np.linalg.norm(matrix @ inputs[-sign]) < 1e-11
        expected = np.sqrt(mass[shift - 1]) * np.exp(1j * phase * shift)
        assert np.linalg.norm(matrix @ inputs[sign] - expected * reference) < 1e-11
    assert np.linalg.eigvalsh(effect).max() <= 1 + 1e-11


for width in (1, 2, 3, 7, 16, 32):
    weights = reference_profile(width, 1)
    observed = program(2, weights).sum()
    expected = np.cos(pi / (width + 2))
    assert abs(observed - expected) < 1e-9, (width, observed, expected)
    verify_instrument(2, weights, np.array([expected]))
for copies in (4, 6):
    for width in (3, 8, 16):
        weights = reference_profile(width, copies)
        mass = even_construction(copies, weights)
        verify_instrument(copies, weights, mass)
        assert program(copies, weights).sum() + 1e-8 >= mass.sum()

print("Direct Kraus completeness, exact orientation return, and zero wrong labels passed.")
print("Two-copy sine-profile LP agreed with the cosine law at six widths.")
for width in (24, 96, 384):
    spacing = pi / (width + 2)
    locations = np.arange(1, width + 2)
    profile = np.sin(spacing * locations) ** 1.05
    weights = profile / profile.sum()
    padded = np.pad(weights, 1)
    neighbors = padded[:-2] + padded[2:]
    denominator = 2 * (weights + np.minimum(padded[:-2], padded[2:]))
    failure = np.max(np.maximum(2 * weights - neighbors, 0) / denominator)
    even, odd = parity_weights(3, weights)
    success_mass = (1 - failure) / 2 * (
        np.pad(weights, (1, 2)) + np.pad(weights, (2, 1))
    )
    assert np.all(success_mass <= 2 * np.minimum(even, odd) + 1e-12)
    assert failure >= (1 - np.cos(spacing)) / (1 + np.cos(spacing)) - 1e-12
    print(f"Three-copy witness N={width}: failure/h^2={failure / spacing ** 2:.6f}")

for width in (16, 32, 64, 128):
    estimates = []
    for copies in (2, 3, 4, 5, 6):
        even = copies - copies % 2
        if even == 2:
            loss = 1 - np.cos(pi / (width + 2))
        else:
            loss = 1 - even_construction(even, reference_profile(width, even)).sum()
        estimates.append(f"k={copies}: {loss:.8g}")
    print(f"N={width} | " + ", ".join(estimates))
