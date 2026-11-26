from itertools import product
from math import pi

import numpy as np


def full_state_response(reference, phase, offsets, true_sign, label, success):
    """Apply the conclusive Kraus row in each total-charge sector."""
    levels = np.arange(reference.size)
    oriented_reference = reference * np.exp(1j * phase * levels)
    signals = [
        np.array([1, true_sign * np.exp(1j * (phase + offset))]) / np.sqrt(2)
        for offset in offsets
    ]
    initial = np.kron(oriented_reference, np.kron(*signals))
    output = np.zeros(reference.size, dtype=complex)
    signal_charges = (0, 1, 1, 2)  # Computational order 00, 01, 10, 11.
    for level in levels:
        total_charge = level + 1
        even = np.zeros(initial.size, dtype=complex)
        odd = np.zeros_like(even)
        for word, signal_charge in enumerate(signal_charges):
            input_level = total_charge - signal_charge
            if 0 <= input_level < reference.size:
                parity = odd if signal_charge % 2 else even
                parity[4 * input_level + word] = reference[input_level] / 2
        even_response = np.vdot(even, initial) / np.vdot(even, even)
        odd_response = np.vdot(odd, initial) / np.vdot(odd, odd)
        output[level] = (
            np.sqrt(success) * reference[level] * (even_response + label * odd_response) / 2
        )
    return oriented_reference, output


def verify_mismatch():
    checked = 0
    for width in (1, 2, 3, 10, 50):
        theta = pi / (width + 2)
        levels = np.arange(width + 1)
        success = np.cos(theta)
        weights = np.sin(theta * (levels + 1))
        weights /= weights.sum()
        reference = np.sqrt(weights) * np.exp(0.23j * levels**2)
        padded = np.pad(weights, 1)
        lower, upper = padded[:-2], padded[2:]
        imbalance = (lower - upper) / (lower + upper)
        moment = weights @ imbalance**2
        for offsets in ((0.01, 0.01), (0.13, -0.21), (1.91, 0.35), (0.0, 0.0)):
            average = (offsets[0] + offsets[1]) / 2
            difference = (offsets[0] - offsets[1]) / 2
            for true_sign, label in product((1, -1), repeat=2):
                original, output = full_state_response(
                    reference, 0.47, offsets, true_sign, label, success
                )
                scalar = np.cos(average) + true_sign * label * np.cos(difference)
                variance = moment * np.sin(average)**2
                expected_probability = success / 4 * (scalar**2 + variance)
                measured_probability = np.vdot(output, output).real
                assert abs(measured_probability - expected_probability) < 2e-14
                if measured_probability > 1e-14:
                    expected_distance_squared = variance / (scalar**2 + variance)
                    measured_fidelity = abs(np.vdot(original, output))**2 / measured_probability
                    assert abs(1 - measured_fidelity - expected_distance_squared) < 2e-14
                checked += 1
    print(f"{checked} full-state two-copy probability and disturbance comparisons passed.")


def verify_squared_sine():
    checked = 0
    for size in (3, 4, 5, 10, 101, 102, 1001, 1002):
        theta = pi / size
        weights = np.sin(theta * np.arange(1, size))**2
        weights /= weights.sum()
        padded = np.pad(weights, 1)
        lower, upper = padded[:-2], padded[2:]
        actual = np.min((lower + upper) / (2 * weights))
        expected = np.cos(theta)**2
        if size % 2:
            expected += np.sin(theta)**2 * np.tan(theta / 2)**2
        assert abs(actual - expected) < 5e-15
        imbalance = (lower - upper) / (lower + upper)
        moment = weights @ imbalance**2
        assert moment <= 4 * np.tan(theta)**2 * (1 - 2 / size) + 1e-12
        if size > 1000:
            assert abs(moment / (4 * theta**2) - 1) < 0.02
        checked += 1
    print(f"{checked} squared-sine optimum and disturbance bounds passed.")


if __name__ == "__main__":
    verify_mismatch()
    verify_squared_sine()
