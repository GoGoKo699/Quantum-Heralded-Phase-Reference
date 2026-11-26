# Quantum Heralded Phase Reference

**Can a finite quantum phase reference read a signal and come back intact?** A charge-conserving receiver can read the binary phase of two identical qubits without ever reporting a wrong label. Whenever it reports a label, it returns the original reference in exactly the same phase-oriented state.

The receiver uses a pure ladder reference on charges $`0,\ldots,N`$ and signal copies with the same unknown common phase. It can abstain. The phase reference may be consumed on an abstention.

| Input batch | Best performance with exact return |
| --- | --- |
| One signal copy | No conclusive outcome is possible. |
| Two signal copies | Success probability $`\cos(\pi/(N+2))`$. |
| Fixed $`k\ge 2`$ copies | Failure probability $`\Theta_k(N^{-2\lfloor k/2\rfloor})`$ as $`N`$ grows. |

For two copies, the optimal reference weights follow a sine profile. The receiver resolves even and odd signal charges coherently inside each total-charge block. An invariant flag records the answer, and the block index remains coherent so the reference can be used again.

The exact-return constraint makes copy parity matter. Three copies halve the leading failure constant while keeping the same exponent as two. Four copies raise the exponent from two to four. A receiver that may discard the reference reaches exponent $`k`$ for every fixed $`k`$. Under small relative phase mismatch, a squared-sine profile suppresses wrong labels and return disturbance more effectively than the success-optimal sine profile. Its leading ideal abstention constant is twice as large.

## Read the science

| Question | Route |
| --- | --- |
| What is the input, and what does exact return guarantee? | [Model and reuse](science/model.md) |
| How does the receiver work, and why is its two-copy probability optimal? | [Finite receiver and charge-transfer program](science/receiver.md) |
| Why do odd batches pay a penalty? | [Copy parity and the disposable reference comparison](science/parity-law.md) |
| What happens if the source and reference phases do not quite match? | [Phase mismatch and reference design](science/phase-mismatch.md) |
| How does this connect to existing measurements and reference frames? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

## Learn the project

The educational anchor is **Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, “Reference frames, superselection rules, and quantum information” (2007)**. The [educational bridge](learning/BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) connects shared phase, charge sectors and relational measurements to the receiver. The [30-milestone map](learning/MILESTONES.md) develops the proofs and their operational consequences in order. [llms.txt](llms.txt) lists reading routes by question.

## Reproduce the finite checks

Run the commands in [Verification](verification/README.md) to reconstruct the receiver, solve finite linear programs and compare the phase mismatch formulas with direct state calculations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
