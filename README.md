# Shifted VT-Codes 
A Shifted VT-Code is an error correcting code that can correct a single insertion or deletion.

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](./CONTRIBUTING.md)

![GitHub repo size](https://img.shields.io/github/repo-size/Guy-Shapira/Shifted-VT-codes?style=plastic)

The redundancy is log(P) + 1, ie. if a given word is of length n, then it can be encoded in n + log(P) + 1 bits st. a single insertion/deletion can be detected and corrected.

this repository implements the algorithms as described in paper: C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, “Codes correcting a burst of deletions or insertions,” IEEE Transactions on Information Theory, vol. 63, no. 4, pp. 1971–1985, Apr. 2017.
# Usage:

## Encoding:
```python
word = [0, 1, 1]
encoder = ShiftedVTCode.ShiftedVTCode(n=7, c=2, d=1, P=5)
codeword = encoder.encode(word)
print(codeword)  # output is '[0, 0, 0, 1, 0, 1, 1]'
```

where n is a length of a codeword, c is the weighted sum, d is the parity and P is the maximum known distance of an error.

## Decoding:
decoding also works if no error has occured, or if a single error (deletion/insertion) has occured.

continuation of the previous example:
```python
word = [0, 1, 1]
encoder = ShiftedVTCode.ShiftedVTCode(n=7, c=2, d=1, P=5)
code = encoder.encode(word)
print(codeword)  # output is '[0, 0, 0, 1, 0, 1, 1]'

# if no error has occured:
decoded = encoder.decode(codeword)
print(decoded)  # output is '[0, 1, 1]'

# if a single error (insertion or deletion) has occured at index 1
decoded = encoder.decode(codeword, u=0)
print(decoded)  # output is '[0, 1, 1]'
```

correcting an insertion or deletion is identical in usage, thus only the index is passed, without the error type.

## Running the tests:
unit tests are provided, and are written using the `unittest` framework built into python.

configure the framework to look for tests in files named `test_*`.
