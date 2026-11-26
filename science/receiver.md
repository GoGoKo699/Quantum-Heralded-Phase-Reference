# A charge-conserving receiver with exact return

The output must retain coherence across reference levels. Work with blocks of fixed total charge, route their amplitudes coherently to the output ladder and record only the sign and charge transferred out of the ladder.

## Parity vectors in each charge block

Let $`|D_j\rangle`$ be the normalized symmetric $`k`$-qubit state with $`j`$ excitations and set $`B_j=2^{-k}\binom{k}{j}`$. At orientation zero the charge-$`q`$ part of the input is $`E_q+sO_q`$, with

```math
E_q=\sum_{j\ \mathrm{even}}c_{q-j}\sqrt{B_j}|q-j\rangle|D_j\rangle,\qquad
O_q=\sum_{j\ \mathrm{odd}}c_{q-j}\sqrt{B_j}|q-j\rangle|D_j\rangle .
```

Use $`e_q=\|E_q\|^2`$ and $`o_q=\|O_q\|^2`$. The vectors are orthogonal and any out-of-range coefficient is zero. A rotation by $`\phi`$ multiplies the whole block by $`e^{iq\phi}`$.

## The finite optimization

For a fixed weight profile, optimize a mass $`p_\ell`$ for each integer charge transfer $`\ell`$. The maximum worst-sign success is the value of the linear program

```math
\begin{aligned}
\text{maximize}\quad &p=\sum_{\ell=1}^{k-1}p_\ell,\qquad p_\ell\ge0,\\
\text{subject to}\quad &
\sum_{\ell=1}^{k-1}p_\ell w_{q-\ell}\le 2\min(e_q,o_q)
\qquad (0\le q\le N+k).
\end{aligned}
```

An empty set of transfers has value zero.

**Necessity.** A finite-dimensional covariant map has a Kraus decomposition into operators of definite charge transfer. This follows by block diagonalizing its Choi operator under the output representation times the conjugate input representation. In the conclusive sign branch every Kraus operator kills the wrong input because the branch output is a sum of positive operators. Each Kraus operator's correct output is parallel to the original reference because that branch returns a pure state.

Let $`a,b`$ be the least and greatest occupied reference charges. At the extreme input charges $`a,b+k`$, the sign vectors are collinear. A Kraus operator with nonzero correct output and charge transfer $`\ell`$ must obtain the reference endpoint amplitudes from input charges $`a+\ell,b+\ell`$. These charges must lie strictly between the extreme input charges. Thus $`1\le\ell\le k-1`$, including when the reference has gaps. After sign symmetrization, the sum of squared correct amplitudes for a given transfer is $`p_\ell`$ for each sign.

In each block, the success effects for the two signs can be restricted to the span of $`E_q,O_q`$. Write $`m_q=\sum_\ell p_\ell w_{q-\ell}`$. The wrong-sign zero and the correct-sign amplitudes fix the sum of the two success effects on that span. Its diagonal entries in the normalized even and odd vectors are $`m_q/(2e_q)`$ and $`m_q/(2o_q)`$. Both must be at most one. If either norm vanishes, the sign vectors are collinear and $`m_q=0`$.

**Construction.** For each label $`s`$ and charge transfer $`\ell`$, use the following Kraus operator, with a zero row if a denominator vanishes.

```math
K_{s,\ell}=\sum_q
  \frac{\sqrt{p_\ell}\,c_{q-\ell}}{2}\,
  |q-\ell\rangle
  \left(\frac{\langle E_q|}{e_q}
       +s\frac{\langle O_q|}{o_q}\right).
```

The term in parentheses has inner product $`2`$ with the block for sign $`s`$ and zero with the opposite sign. It follows directly that

```math
K_{s,\ell}|\Psi_{s,\phi}\rangle
  =\sqrt{p_\ell}\,e^{i\ell\phi}|R_\phi\rangle,\qquad
K_{s,\ell}|\Psi_{-s,\phi}\rangle=0.
```

Summing the effects of the two signs cancels the off-diagonal parity terms. At each charge the two nonzero eigenvalues are the entries above, so the finite inequalities imply that the total effect is at most the identity. This also gives a conserving implementation as a block isometry. On success send a charge-$`\ell`$ environment record and an invariant sign flag. On failure send the output reference to its level zero and copy the input after applying the square root of the complement effect into an environment with charge matching the input. Orthogonal output flags complete the isometry, which can be extended within charge sectors after adding invariant workspace. The charge block index itself stays coherent throughout the success operation.

## Optimizing the two-copy receiver

Only transfer $`\ell=1`$ is possible. In terms of $`i=q-1`$, the constraints are $`p\le1`$ and

```math
p w_i \le \frac{w_{i-1}+w_{i+1}}{2},\qquad 0\le i\le N.
```

Let $`A`$ be half the adjacency matrix of the path on $`0,\ldots,N`$. Its positive eigenvector $`v_i=\sin((i+1)\pi/(N+2))`$ has eigenvalue $`\lambda=\cos(\pi/(N+2))`$. Taking the inner product of $`pw\le Aw`$ with $`v`$ gives $`p\le\lambda`$ for every admissible profile since $`v^T w>0`$. Setting $`w_i=v_i/\sum_j v_j`$ saturates the constraints at $`p=\lambda`$. The charge amplitudes of one attaining pure reference are $`\sqrt{w_i}`$.

For example, the two-level reference uses equal weights and returns exactly with probability $`1/2`$. With three levels the weights are proportional to $`(1,\sqrt{2},1)`$ and success is $`1/\sqrt{2}`$. For large $`N`$ the per-attempt failure is $`\pi^2/[2(N+2)^2]+O(N^{-4})`$.

[Model](model.md) · [Parity law](parity-law.md) · [Finite verification](../verification/README.md)
