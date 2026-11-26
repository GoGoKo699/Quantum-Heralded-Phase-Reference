# Verification

From the repository root with Python 3.11 or later, install the numerical dependencies in your chosen environment and run both checks.

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/check_receiver.py
python3 verification/check_phase_mismatch.py
```

The receiver check constructs the conclusive Kraus operators on finite charge ladders. It tests completeness, annihilation of the wrong sign and vector-level return of the reference at nonzero common phase. It also solves the fixed-profile linear program at six widths for two copies and compares with the cosine law. It verifies the explicit three-copy witness and the finite converse at three widths. Its larger-width table gives achievable witness failures. For more than two copies, the table uses the sine-power construction and discards the extra copy of an odd batch.

The mismatch check applies the two-copy Kraus matrices in the full signal space, including unequal phase offsets and arbitrary reference phases. It compares conclusive probabilities and conditional return distance with the formulas and checks the squared-sine profile. Success messages from both scripts summarize the compared cases.

The finite checks supplement the analytical [receiver proof](../science/receiver.md), [copy-parity asymptotics](../science/parity-law.md) and [phase mismatch bounds](../science/phase-mismatch.md).
