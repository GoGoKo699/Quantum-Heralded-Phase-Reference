# Project understanding map with 30 milestones

The background phase connects the preparation and symmetry to the full receiver contract in 12 milestones. The narrative phase uses 18 milestones to build the receiver, compare it with disposable readout, and explain how exact return changes repeat use and copy scaling.

The [bridge to Bartlett, Rudolph, and Spekkens](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) gives the single educational anchor and its relevant sections. Each milestone points to the project sources that develop its understanding target.

| Phase | Milestones | Theme |
|---|---|---|
| Background and preliminaries | [M01](#m01-one-shared-unknown-phase)–[M06](#m06-covariant-operations-and-flags) | Phase, charge, and covariant operations |
| Background and preliminaries | [M07](#m07-signal-parity-within-one-sector)–[M12](#m12-the-complete-receiver-contract) | Unambiguous readout, conditional states, and the receiver contract |
| Narrative and innovation | [M13](#m13-the-sector-success-budget)–[M17](#m17-completing-the-instrument) | Sector bounds, conclusive branches, and instrument completeness |
| Narrative and innovation | [M18](#m18-one-copy-versus-two)–[M20](#m20-the-two-copy-equality-construction) | Smallest example and exact two-copy optimum |
| Narrative and innovation | [M21](#m21-the-reusable-receiver-versus-disposable-readout)–[M25](#m25-the-parity-law-in-one-comparison) | Matched disposable and parity-dependent return laws |
| Narrative and innovation | [M26](#m26-a-sequence-of-successful-labels)–[M30](#m30-the-complete-scientific-story) | Repeat use, mismatch, attribution, and synthesis |

## Background and preliminaries

### M01 One shared unknown phase

**Central question.** What changes when the receiver chooses a different phase origin?

**Understanding target.** Represent a phase shift by charge-dependent factors and identify the sign as a relative half-turn. The receiver has one unknown common angle for the reference and signals.

**Dependencies.** Starts the map.

**Conceptual connection.** A common change of origin preserves the two label hypotheses as distinct relational preparations.

**Sources.** [Model](../science/model.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M02 A finite quantum reference

**Central question.** What kind of state carries the receiver's phase information?

**Understanding target.** Describe the pure reference by ladder amplitudes and their squared magnitudes, normalized on charges zero through the cutoff. A charge eigenstate alone provides no phase comparison.

**Dependencies.** [M01](#m01-one-shared-unknown-phase)

**Conceptual connection.** The amplitudes carry orientation and their squared magnitudes determine the weights available to each charge sector.

**Sources.** [Model](../science/model.md)

### M03 Identical copies and signal charge

**Central question.** How do several signals distribute their total charge?

**Understanding target.** Group the tensor product by excitation number. The normalized symmetric vector in each group is weighted by the square root of its binomial probability, and the unknown sign is raised to the group's charge.

**Dependencies.** [M01](#m01-one-shared-unknown-phase)

**Conceptual connection.** Different numbers of signal qubits change the multiplicities and the signs of sector terms in a predictable way.

**Sources.** [Model](../science/model.md)

### M04 Total charge sectors

**Central question.** Which combinations of reference and signal can interfere?

**Understanding target.** For each total charge, collect all ways to split it between the reference and signal register. A joint phase change multiplies that entire sector by a common factor.

**Dependencies.** [M02](#m02-a-finite-quantum-reference), [M03](#m03-identical-copies-and-signal-charge)

**Conceptual connection.** The different charge splits in a single sector can carry different powers of the sign, which makes relative discrimination possible.

**Sources.** [Model](../science/model.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M05 Joint phase averaging

**Central question.** Why does a shared phase matter even when it is unknown?

**Understanding target.** Explain why averaging jointly over the phase deletes cross-sector coherences while retaining within-sector coherences. Averaging each register independently can delete the relative-sign information.

**Dependencies.** [M04](#m04-total-charge-sectors)

**Conceptual connection.** The average may be used for invariant outcome probabilities. The pure reference return is a condition on each physical phase orientation.

**Sources.** [Model](../science/model.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M06 Covariant operations and flags

**Central question.** How can a receiver work at every orientation without a hidden reference?

**Understanding target.** Describe covariance as equivariance under rotation of input and output. A sign flag or abstention flag is invariant, while the output reference transforms with its charge.

**Dependencies.** [M04](#m04-total-charge-sectors), [M05](#m05-joint-phase-averaging)

**Conceptual connection.** A charge reservoir in a definite-charge state may take a known displacement without introducing another phase standard.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

### M07 Signal parity within one sector

**Central question.** Where exactly do the two labels differ in a sector?

**Understanding target.** Split the sector into orthogonal even and odd signal-charge components. The two sign vectors add those components with opposite relative signs.

**Dependencies.** [M03](#m03-identical-copies-and-signal-charge), [M04](#m04-total-charge-sectors)

**Conceptual connection.** The sector can distinguish the labels only if it has both components, which immediately exposes the extreme-charge constraint.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

### M08 Unambiguous discrimination

**Central question.** What can the receiver do when two state vectors overlap?

**Understanding target.** Distinguish a wrong reported sign from abstention. The former must have probability zero for the exact task. A conclusive effect must annihilate the input vector of the other sign.

**Dependencies.** [M07](#m07-signal-parity-within-one-sector)

**Conceptual connection.** This is why a sector with only one parity has no conclusive sign probability, even though charge can be measured there.

**Sources.** [Receiver](../science/receiver.md) · [Related work](../references/RELATED_WORK.md)

### M09 Effects and output operations

**Central question.** What does a measurement description need to specify when a reference must be returned?

**Understanding target.** Separate a positive outcome effect, which defines a probability, from the operation that also defines the output state for that outcome.

**Dependencies.** [M06](#m06-covariant-operations-and-flags), [M08](#m08-unambiguous-discrimination)

**Conceptual connection.** Sector probabilities alone cannot guarantee a coherent reference output. The receiver proof works with Kraus operations and their output amplitudes.

**Sources.** [Receiver](../science/receiver.md)

### M10 One charge displacement per Kraus mode

**Central question.** How can a successful amplitude preserve coherence between different input sectors?

**Understanding target.** Understand how a charge-shift Kraus operator maps each input charge to its corresponding output charge, with the same displacement in every sector.

**Dependencies.** [M06](#m06-covariant-operations-and-flags), [M09](#m09-effects-and-output-operations)

**Conceptual connection.** The discarded system can carry a definite displacement. A record distinguishing different input charges within that displacement can destroy the coherence needed for return.

**Sources.** [Receiver](../science/receiver.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M11 Exact return and conditional reuse

**Central question.** What precisely qualifies the reference for another run?

**Understanding target.** On either reported sign, the reference must have the same normalized pure state as before the operation at the actual shared phase. Abstention and resource use remain part of the protocol.

**Dependencies.** [M02](#m02-a-finite-quantum-reference), [M09](#m09-effects-and-output-operations), [M10](#m10-one-charge-displacement-per-kraus-mode)

**Conceptual connection.** Pure return keeps the reference uncorrelated with discarded systems on a conclusive branch, so it can meet the same input contract again.

**Sources.** [Model](../science/model.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M12 The complete receiver contract

**Central question.** Which resources and performance criteria define the comparison?

**Understanding target.** Assemble the finite charge cutoff, the number of supplied copies per attempt, joint symmetry, the zero-error label condition, and exact conclusive return. Identify success probability as the optimized quantity.

**Dependencies.** [M05](#m05-joint-phase-averaging), [M08](#m08-unambiguous-discrimination), [M11](#m11-exact-return-and-conditional-reuse)

**Conceptual connection.** This contract fixes what an implementation can spend and what it must produce, including the conditions on any reused reference.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md)

## Narrative and innovation

### M13 The sector success budget

**Central question.** How much conclusive probability can one charge sector supply?

**Understanding target.** Use the orthogonal even and odd components and sign symmetry to explain the budget $`2\min(e_q,o_q)`$. Here $`e_q`$ and $`o_q`$ are squared norms in an unnormalized sector.

**Dependencies.** [M07](#m07-signal-parity-within-one-sector), [M08](#m08-unambiguous-discrimination), [M12](#m12-the-complete-receiver-contract)

**Conceptual connection.** This sector budget measures the mass available for each returned-reference amplitude in the converse.

**Sources.** [Receiver](../science/receiver.md)

### M14 The extreme charges exclude shifts

**Central question.** Why can successful charge displacements neither vanish nor exhaust all signal charge?

**Understanding target.** Track the minimum and maximum nonzero charges in the input reference. Matching the returned reference makes every successful displacement enter the interior of the joint total-charge interval.

**Dependencies.** [M10](#m10-one-charge-displacement-per-kraus-mode), [M11](#m11-exact-return-and-conditional-reuse), [M13](#m13-the-sector-success-budget)

**Conceptual connection.** An extreme input sector has collinear sign vectors. The allowed shifts are one through one less than the number of copies, even if the reference has gaps.

**Sources.** [Receiver](../science/receiver.md)

### M15 The fixed-profile linear program

**Central question.** How do different successful shifts compete for the same sector?

**Understanding target.** Read the shifted reference probabilities as mass requirements and the parity budget as capacity. Sum the shift-specific requirements at each input charge and maximize total successful mass subject to the inequalities.

**Dependencies.** [M13](#m13-the-sector-success-budget), [M14](#m14-the-extreme-charges-exclude-shifts)

**Conceptual connection.** The linear program fixes the reference profile. Optimizing that profile is a separate outer problem.

**Sources.** [Receiver](../science/receiver.md)

### M16 A conclusive branch that realizes the program

**Central question.** How does a feasible mass assignment become a receiver?

**Understanding target.** In each sector, combine the normalized even and odd dual directions so that one reported sign adds the components and the other cancels. Send the survivor to the charge fixed by the displacement.

**Dependencies.** [M09](#m09-effects-and-output-operations), [M10](#m10-one-charge-displacement-per-kraus-mode), [M15](#m15-the-fixed-profile-linear-program)

**Conceptual connection.** The same correct-sign amplitude pattern is reproduced across the ladder. Changing the shared phase contributes only the prescribed reference phase and a common factor for each shift.

**Sources.** [Receiver](../science/receiver.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M17 Completing the instrument

**Central question.** Why does the explicit receiver have a physical abstention branch?

**Understanding target.** Sum the positive effects from both sign outcomes and all displacements. The even–odd cross terms cancel and the linear program bounds both remaining diagonal terms by one.

**Dependencies.** [M13](#m13-the-sector-success-budget), [M15](#m15-the-fixed-profile-linear-program), [M16](#m16-a-conclusive-branch-that-realizes-the-program)

**Conceptual connection.** The remaining positive effect completes the receiver. A conserving dilation can store the displacement without reading the input charge.

**Sources.** [Receiver](../science/receiver.md)

### M18 One copy versus two

**Central question.** Why are two signals the first possible reusable readout?

**Understanding target.** Compare the empty shift set for one copy with the single allowed shift for two. Follow the two nontrivial sectors in the two-level reference example and verify that the wrong sign cancels in both.

**Dependencies.** [M14](#m14-the-extreme-charges-exclude-shifts), [M16](#m16-a-conclusive-branch-that-realizes-the-program), [M17](#m17-completing-the-instrument)

**Conceptual connection.** The smallest example links the support obstruction to an implementation that succeeds with probability one half.

**Sources.** [Receiver](../science/receiver.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) · [Verification](../verification/README.md)

### M19 The path averaging bound

**Central question.** Why does the two-copy optimum depend on a cosine?

**Understanding target.** Write the success condition as a neighboring-charge average. Use a positive left eigenvector of the path averaging matrix to bound success for every nonnegative normalized weight profile.

**Dependencies.** [M15](#m15-the-fixed-profile-linear-program), [M18](#m18-one-copy-versus-two)

**Conceptual connection.** At two copies, the charge-sector constraints become a single spectral problem over the whole ladder.

**Sources.** [Receiver](../science/receiver.md)

### M20 The two-copy equality construction

**Central question.** Which reference attains the two-copy limit?

**Understanding target.** Take the reference probabilities proportional to the path sine eigenvector and the amplitudes as square roots of those probabilities. Check that all neighboring-charge inequalities are tight.

**Dependencies.** [M16](#m16-a-conclusive-branch-that-realizes-the-program), [M17](#m17-completing-the-instrument), [M19](#m19-the-path-averaging-bound)

**Conceptual connection.** This closes the converse and construction at every cutoff, including the degenerate one-level boundary.

**Sources.** [Receiver](../science/receiver.md) · [Verification](../verification/README.md)

### M21 The reusable receiver versus disposable readout

**Central question.** What changes if the receiver can discard the reference?

**Understanding target.** Optimize sector measurements independently once coherent output is unnecessary. The residual failure becomes a sum of absolute even–odd differences over all sectors.

**Dependencies.** [M12](#m12-the-complete-receiver-contract), [M13](#m13-the-sector-success-budget), [M17](#m17-completing-the-instrument)

**Conceptual connection.** This comparison uses the same signal promise and cutoff, so the gap isolates the effect of the return contract.

**Sources.** [Parity law](../science/parity-law.md) · [Related work](../references/RELATED_WORK.md)

### M22 Finite differences and the disposable exponent

**Central question.** Why does the disposable failure scale with the number of copies?

**Understanding target.** Connect alternating binomial coefficients with a finite difference of that order. A Fourier test at inverse ladder width gives a lower bound, and smooth ladder profiles give the matching upper bound.

**Dependencies.** [M03](#m03-identical-copies-and-signal-charge), [M21](#m21-the-reusable-receiver-versus-disposable-readout)

**Conceptual connection.** This gives the baseline for every fixed copy count, which can then be compared with the even and odd exact-return receivers.

**Sources.** [Parity law](../science/parity-law.md)

### M23 An even-copy receiver with high success

**Central question.** How can extra pairs of signals improve exact-return scaling?

**Understanding target.** Choose successful shifts from the odd part of the signal-charge distribution. For even copy count, those shifts avoid both endpoints. A smooth probability profile controls the required sector inequalities.

**Dependencies.** [M15](#m15-the-fixed-profile-linear-program), [M16](#m16-a-conclusive-branch-that-realizes-the-program), [M22](#m22-finite-differences-and-the-disposable-exponent)

**Conceptual connection.** The edge behavior of the smooth profile and the charge parity together allow exact return at the same leading order as disposable readout in this regime.

**Sources.** [Parity law](../science/parity-law.md) · [Verification](../verification/README.md)

### M24 The odd-copy obstruction

**Central question.** Why does one extra copy fail to change the exact-return exponent?

**Understanding target.** Identify the nonnegative residual between total sector mass and requested successful mass. A polynomial vanishing on the interior shift set isolates the two extreme signal charges when the number of copies is odd.

**Dependencies.** [M14](#m14-the-extreme-charges-exclude-shifts), [M15](#m15-the-fixed-profile-linear-program), [M22](#m22-finite-differences-and-the-disposable-exponent)

**Conceptual connection.** The polynomial witness is sensitive to the return condition and rules out the faster disposable exponent even with a free choice of reference profile.

**Sources.** [Parity law](../science/parity-law.md)

### M25 The parity law in one comparison

**Central question.** How do the fixed-copy regimes fit into one scaling law?

**Understanding target.** At fixed copy count and increasing ladder width, combine the even construction and odd converse with the strategy that ignores the last odd copy. Identify the best guaranteed exponent as the largest even integer no greater than the supplied copy count, for counts of at least two.

**Dependencies.** [M20](#m20-the-two-copy-equality-construction), [M22](#m22-finite-differences-and-the-disposable-exponent), [M23](#m23-an-even-copy-receiver-with-high-success), [M24](#m24-the-odd-copy-obstruction)

**Conceptual connection.** The exact-return cost appears as a lost power of ladder width at odd copy counts. Finite-size constants can still benefit from an extra copy.

**Sources.** [Parity law](../science/parity-law.md) · [Verification](../verification/README.md)

### M26 A sequence of successful labels

**Central question.** What does exact return buy across repeated attempts?

**Understanding target.** For fresh aligned batches and a common success probability, explain why the chance of reaching a chosen number of conclusive labels before abstention is the corresponding power of that probability.

**Dependencies.** [M11](#m11-exact-return-and-conditional-reuse), [M17](#m17-completing-the-instrument), [M25](#m25-the-parity-law-in-one-comparison)

**Conceptual connection.** The pure reference is available after every conclusive run. Each fresh signal batch is charged and a sequence can terminate on the first abstention.

**Sources.** [Model](../science/model.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M27 Relative phase mismatch

**Central question.** What fails if the reference and signals no longer share an exact phase?

**Understanding target.** Separate an unknown common rotation from an unknown signal-only offset. Use the mismatch analysis to distinguish a wrong label, abstention, and disturbance conditioned on a reported label. Understand how the squared-sine probability profile trades some ideal success for lower sensitivity.

**Dependencies.** [M01](#m01-one-shared-unknown-phase), [M05](#m05-joint-phase-averaging), [M16](#m16-a-conclusive-branch-that-realizes-the-program), [M26](#m26-a-sequence-of-successful-labels)

**Conceptual connection.** The exact theorem uses a sharp preparation promise. A mismatch analysis tests that promise by changing the state family in a controlled way.

**Sources.** [Phase mismatch](../science/phase-mismatch.md)

### M28 Which results come from which source?

**Central question.** Where do the symmetry tools end and the reusable-receiver argument begin?

**Understanding target.** Separate the review's relational phase framework and standard sector discrimination from the project's exact return constraints, charge-shift program, and parity comparison.

**Dependencies.** [M06](#m06-covariant-operations-and-flags), [M08](#m08-unambiguous-discrimination), [M15](#m15-the-fixed-profile-linear-program), [M25](#m25-the-parity-law-in-one-comparison)

**Conceptual connection.** These distinctions let readers compare protocols that either tolerate disturbance, supply a new coherent state, or recover the same phase reference on a conclusive outcome.

**Sources.** [Related work](../references/RELATED_WORK.md) · [Anchor bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M29 Finite checks and proof scope

**Central question.** What can a numerical reconstruction establish?

**Understanding target.** Read the verification route as a check of finite examples, program optima at selected fixed profiles, and finite operators. Locate the analytic steps needed for universality and asymptotic claims.

**Dependencies.** [M17](#m17-completing-the-instrument), [M20](#m20-the-two-copy-equality-construction), [M25](#m25-the-parity-law-in-one-comparison), [M27](#m27-relative-phase-mismatch)

**Conceptual connection.** The proofs explain the cutoff and copy regimes. The finite checks help verify that the implementing matrices and computed examples follow those definitions.

**Sources.** [Verification](../verification/README.md) · [Receiver](../science/receiver.md) · [Parity law](../science/parity-law.md)

### M30 The complete scientific story

**Central question.** How can a finite phase reference reveal a sign without being altered on success?

**Understanding target.** Reconstruct the argument from shared phase through sector discrimination, coherent charge displacement, and exact conclusive return. Explain the two-copy success optimum, the odd-copy penalty, and what changes when exact alignment or return is relaxed.

**Dependencies.** [M12](#m12-the-complete-receiver-contract), [M20](#m20-the-two-copy-equality-construction), [M21](#m21-the-reusable-receiver-versus-disposable-readout), [M25](#m25-the-parity-law-in-one-comparison), [M26](#m26-a-sequence-of-successful-labels), [M27](#m27-relative-phase-mismatch), [M29](#m29-finite-checks-and-proof-scope)

**Conceptual connection.** The story connects an explicit receiver with its converse, the accounting for fresh coherent signals, and the limits of what can be inferred under different promises.

**Sources.** [Model](../science/model.md) · [Receiver](../science/receiver.md) · [Parity law](../science/parity-law.md) · [Phase mismatch](../science/phase-mismatch.md)
