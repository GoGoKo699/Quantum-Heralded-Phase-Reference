# From quantum reference frames to a reusable phase receiver

Two sources share a phase setting the receiver does not know. One gives the receiver a finite quantum reference. The other sends copies of a qubit with either the same phase or a phase shifted by half a turn. The receiver must report the relative sign or abstain. Every time it reports a sign, it must return the original reference with its phase intact so it can be used again.

The educational anchor is Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, **Reviews of Modern Physics 79**, 555–609 (2007). Section numbers refer to the published version. [DOI](https://doi.org/10.1103/RevModPhys.79.555) · [Full text](https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.79.555/fulltext)

| Published sections | What they contribute | Where to use them |
|---|---|---|
| II.A–C | Changing a phase origin, averaging over a common unknown phase, and identifying invariant total-charge sectors | [M01–M05](MILESTONES.md#m01-one-shared-unknown-phase) |
| IV.A.1 and IV.A.4 | Treating the reference as a quantum system and locating relational information in a composite system | [M04–M08](MILESTONES.md#m04-total-charge-sectors) |
| VI.A.2 | Interpreting a joint measurement as measurement of a relative quantity | [M07–M10](MILESTONES.md#m07-signal-parity-within-one-sector) |
| VI.B.2 | Understanding how using a bounded reference can affect its future use | [M11–M12](MILESTONES.md#m11-exact-return-and-conditional-reuse) and [M26](MILESTONES.md#m26-a-sequence-of-successful-labels) |

The review supplies the symmetry and measurement perspective. The return condition, the resulting linear program, and the copy-parity law are developed in the project. [Model](../science/model.md) · [Receiver](../science/receiver.md) · [Parity law](../science/parity-law.md) · [Related work](../references/RELATED_WORK.md)

## Turn the shared phase into a charge constraint

The review writes a phase shift as $`U(\phi)=\exp(i\phi\hat N_{\mathrm{tot}})`$ and gives the total photon number as an example of its generator. Here one counts integer charges. The reference has eigenstates $`\lvert i\rangle`$ for $`0\le i\le N`$, and each signal qubit has charges zero and one. The integer $`q`$ is the sum of reference and signal charges. Each component in sector $`q`$ acquires the same factor $`e^{iq\phi}`$ under a shift of the shared phase. The sign $`s\in\{+1,-1\}`$ in the signal is the relative label, so it is unchanged by this shift.

Averaging over the shared phase deletes off-diagonal density-matrix blocks between different $`q`$. Inside any one sector, a reference component and a signal component whose charges add up to $`q`$ can interfere. For example, a charge-one reference and a charge-zero signal can interfere with a charge-zero reference and a charge-one signal. Independently averaging the reference and signal phases would remove that interference. The project uses a common phase and tools that respect the resulting $`U(1)`$ symmetry. [Model](../science/model.md)

A classical flag records a sign or an abstention. The mathematical description of a flag includes both its probability and its output state. With the reference discarded, the receiver can use an independent optimal discrimination measurement inside each charge sector. To return the reference, amplitudes from different input sectors must reach the corresponding output charges with one fixed displacement, with coherence across those output charges. A success operation may put the displacement into a definite-charge environment state. Reading or leaking the input charge itself can erase the output coherence. [Receiver](../science/receiver.md)

## Work through the smallest reusable receiver

Use a two-level reference, $`N=1`$, with equal charge probabilities and two identical signals of sign $`s`$. At common phase zero, write $`\lvert i,D_j\rangle`$ for reference charge $`i`$ and the normalized symmetric two-qubit state with signal charge $`j`$. In particular, $`\lvert D_1\rangle=(\lvert 01\rangle+\lvert 10\rangle)/\sqrt{2}`$. The two sectors that can reveal the sign have the following input amplitudes.

| Total charge | Even signal charge component | Odd signal charge component | Returned charge |
|---|---|---|---|
| 1 | $`\lvert 1,D_0\rangle/(2\sqrt{2})`$ | $`s\lvert 0,D_1\rangle/2`$ | 0 |
| 2 | $`\lvert 0,D_2\rangle/(2\sqrt{2})`$ | $`s\lvert 1,D_1\rangle/2`$ | 1 |

On either row the operation for a reported sign $`a\in\{+1,-1\}`$ multiplies the even basis coefficient by $`1/\sqrt{2}`$ and the odd basis coefficient by $`a/2`$. These terms add to $`(1+as)/4`$ in the indicated returned charge. Thus the operation cancels the wrong sign on both rows. The sum of the two conclusive effects has eigenvalue one in each even direction and one half in each odd direction, so there is room for a positive abstention effect. The split between the two signs comes from interference, while the completeness condition comes from summing both possible effects.

With the correct sign and common phase $`\phi`$, these two rows together give the unnormalized output

```math
\frac{e^{i\phi}}{2}\bigl(\lvert 0\rangle+e^{i\phi}\lvert 1\rangle\bigr).
```

The squared norm is one half. The normalized state agrees with the input reference up to an overall phase. At both input extremes, charges zero and three, the two sign vectors are proportional, so those sectors give no conclusive amplitude. With a single signal there are still only two extremes, with an interval between them too short to match the full span of the original reference at any fixed displacement. [Receiver](../science/receiver.md) · [Finite checks](../verification/README.md)

## From the example to the copy-parity law

For higher charge cutoffs the input in sector $`q`$ has orthogonal even and odd components, with squared norms $`e_q`$ and $`o_q`$. Zero-error discrimination gives that sector a maximum conclusive probability mass of $`2\min(e_q,o_q)`$. The output reference prescribes a required mass in every sector reached by a candidate displacement. The pointwise compatibility of supply and demand is the linear program in the [receiver proof](../science/receiver.md).

With two signals there is just one possible displacement. The resulting inequality compares each ladder weight with the average of its neighbors. A positive sine eigenvector of this averaging operation makes all the inequalities tight and gives the optimal success probability. With more copies the two parities supply shifted binomial sums. Their difference is a finite difference. Smooth ladder profiles make this difference small, and the support restriction on successful displacements supplies the extra odd-copy bound. [Parity law](../science/parity-law.md)

The endpoint concerns exact return on conclusive runs. The apparatus consumes a fresh batch of phase-aligned signals per attempt, includes abstention in its accounting, and may lose the reference on abstention. Unknown relative phase offset changes the hypotheses themselves. For two copies, changing the reference probabilities from a sine to its square increases ideal abstention but reduces the sensitivity of the returned state to a small relative offset. [Phase mismatch](../science/phase-mismatch.md) · [30-milestone map](MILESTONES.md)
