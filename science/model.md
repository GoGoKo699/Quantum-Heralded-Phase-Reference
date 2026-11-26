# Reading a phase without spending the reference on success

A qubit arriving in one of two opposite equatorial states encodes a sign. A receiver without the source's phase convention needs a physical reference to interpret the sign. We consider a receiver that can decline to answer. A conclusive answer must be correct and leave the reference ready for the next batch in exactly its input state.

## Inputs and operations

The finite reference has nondegenerate charge levels $`0,\ldots,N`$ and a supplied pure template. The receiver knows its coefficients $`c_i`$ and uses the same instrument at every orientation $`\phi`$. A batch contains $`k`$ copies with the same hidden sign $`s\in\{+1,-1\}`$ and the same orientation as the reference.

```math
|R_\phi\rangle=\sum_{i=0}^N c_i e^{\mathrm{i}i\phi}|i\rangle,\qquad
|s_\phi\rangle=\frac{|0\rangle+s e^{\mathrm{i}\phi}|1\rangle}{\sqrt 2},
\qquad |\Psi_{s,\phi}\rangle=|R_\phi\rangle\otimes |s_\phi\rangle^{\otimes k}.
```

The reference weights $`w_i=|c_i|^2`$ sum to one and extend by zero outside the ladder. The signal charge counts excitations. The joint symmetry acts at total charge $`Q`$ by the phase factor $`e^{\mathrm{i}Q\phi}`$. Each operation labeled $`+,-,?`$ is completely positive and covariant, and the three operations sum to a trace-preserving channel. The flags are invariant. An implementation may use a charge-conserving unitary, an initially invariant ancillary state and an invariant readout. Coherence shared with the source enters through the supplied reference and the $`k`$ signals.

Writing $`\rho_R(\phi)=|R_\phi\rangle\langle R_\phi|`$, a conclusive branch has the contract

```math
\mathcal I_s(|\Psi_{s,\phi}\rangle\langle\Psi_{s,\phi}|)
   = p_s\,\rho_R(\phi),\qquad
\mathcal I_s(|\Psi_{-s,\phi}\rangle\langle\Psi_{-s,\phi}|)=0 .
```

We maximize $`\min(p_+,p_-)`$. Covariance makes each probability independent of $`\phi`$. Conjugating by signal parity flips the hypotheses, so that shared classical randomization and relabeling yield an equal-probability optimum. On success the pure returned reference factors from the remaining outputs, including any discarded environment. The failure branch is unrestricted. This is exact return for the supplied orbit of a known template. The contract consumes the signals and allows them to provide coherence during the measurement.

## Results and scope

| Signal batch | Optimal result with exact return |
| --- | --- |
| One copy | Zero conclusive probability on every finite ladder. |
| Two copies | Optimal success $`\cos(\pi/(N+2))`$. The optimal weights are proportional to $`\sin((i+1)\pi/(N+2))`$. |
| Any fixed $`k\ge2`$ | Optimized failure $`\Theta_k(N^{-2\lfloor k/2\rfloor})`$ as $`N`$ grows. |

The [receiver construction](receiver.md) gives the complete finite program for a fixed profile and the optimizing two-copy measurement. The [parity law](parity-law.md) compares exact return with the same measurement when its reference may be discarded. The latter allows failure $`\Theta_k(N^{-k})`$ for either parity. The [phase mismatch analysis](phase-mismatch.md) separates false labels, abstention and return error when the alignment promise is imperfect.

## Repeated use

Feed a fresh phase-aligned batch after each conclusive result. With the symmetric receiver and fixed per-batch success probability $`p`$, at least $`m`$ correct labels are produced before the first abstention with probability $`p^m`$. The mean number of correct labels before that first abstention is $`p/(1-p)`$. Each attempt consumes $`k`$ new signal qubits, including the last attempt. The failure law therefore characterizes the lifetime of one supplied reference with this reuse rule. Preparing a reference, keeping the phases aligned, implementing the coherent blocks and recovering a reference after an abstention are separate costs. A run with a uniformly random common phase is described by averaging the pointwise results over that phase.

[Receiver](receiver.md) · [Parity law](parity-law.md) · [Related work](../references/RELATED_WORK.md)
