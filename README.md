A Shifted VT-Code is an error correcting code that can correct a single insertion or deletion.

The redundancy is log(P) + 1, ie. if a given word is of length n, then it can be encoded in n + log(P) + 1 bits st. a single insertion/deletion can be detected and corrected.

this repository implements the algorithms as described in the article (by Clayton Schoeny, Antonia Wachter-Zeh, Ryan Gabrys, Eitan Yaakobi) 'Codes Correcting a Burst of Deletions or Insertions' in subsection 4b: https://arxiv.org/abs/1602.06820

# Usage:

## Encoding:
`word
encoder = ShiftedVTCode.ShiftedVTCode(n, c, d, P)
encoder.encode(` where n is a length of a codeword
