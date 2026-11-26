# Related work

The reference is a physical part of the input. Its exact return is required on each label branch so that the same reference can read the next batch. The [measurement](../science/receiver.md) borrows charge-sector discrimination tools and adds a coherent output constraint.

## Constrained measurements and reference states

[Ahmadi, Jennings and Rudolph, “The Wigner–Araki–Yanase theorem and the quantum resource theory of asymmetry”](https://doi.org/10.1088/1367-2630/15/1/013057) develops the reduction from conserved-charge measurement to discrimination in invariant sectors and constructs optimal instruments for selected qubit tasks. Section 3.1 discusses restoring the measured signal on a success branch by swapping in a paid additional coherent qubit. Here the returned system is the prepared reference ladder. Its level weights must be supplied by an allowed coherent charge transfer, as expressed by the pointwise constraints in the receiver program. Their minimum-error sine-amplitude reference and the sine-weight reference for our two-copy exact-return objective solve different optimizations.

[Van Enk, “Quantifying the resource of sharing a reference frame”](https://arxiv.org/abs/quant-ph/0410083) develops refbit-assisted unambiguous discrimination as a communication primitive. The refbits help identify a signal and are spent by the protocol. When reference discarding is allowed here, the familiar sector discrimination formula yields the finite-difference benchmark in the [copy-parity analysis](../science/parity-law.md).

[Gour and Spekkens, “The resource theory of quantum reference frames”](https://doi.org/10.1088/1367-2630/10/3/033023) characterizes covariant Kraus operators by charge shifts and treats stochastic transformations of a supplied pure state. The present two-label problem imposes two conditions on every conclusive Kraus operator: it kills the opposite sign and restores the reference coherent amplitudes on the correct sign. Their conjunction excludes both endpoint shifts and leads to the finite program.

## Repeated use and limits

[Bartlett, Rudolph, Spekkens and Turner, “Degradation of a quantum reference frame”](https://doi.org/10.1088/1367-2630/8/4/058) studies bounded-error longevity for phase and direction references changed by successive measurements. Here the output flag distinguishes exact successful reuse from the first abstention. Fresh batches carry the phase resource and are charged on every attempt.

[Lostaglio and Müller, “Coherence and asymmetry cannot be broadcast”](https://doi.org/10.1103/PhysRevLett.123.020403) constrains deterministic broadcasting of asymmetry from a finite-dimensional source. The output label here is invariant, each incoming batch is already asymmetric, and the reference may be lost on the recorded failure branch.

The educational anchor, [Bartlett, Rudolph and Spekkens, “Reference frames, superselection rules, and quantum information”](https://doi.org/10.1103/RevModPhys.79.555), provides the operational interpretation of the shared unknown phase and of measurements with finite references. The project's [bridge](../learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) identifies the relevant sections.

[Bibliography](references.bib) · [Model](../science/model.md)
