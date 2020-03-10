A Shifted VT-Code is an error correcting code that can correct a single insertion or deletion.

The redundancy is log(P) + 1, ie. if a given word is of length n, then it can be encoded in n + log(P) + 1 bits st. a single insertion/deletion can be detected and corrected.

this repository implements the algorithms as described in the  C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, “Codes correcting a burst of deletions or insertions,” IEEE Transactions on Information Theory, vol. 63, no. 4, pp. 1971–1985, Apr. 2017.
# Usage:

## Encoding:
`word
encoder = ShiftedVTCode.ShiftedVTCode(n, c, d, P)
encoder.encode(` where n is a length of a codeword
