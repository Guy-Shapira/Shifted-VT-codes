from math import log2 as log, ceil
from typing import List
from utils import weighted_sum, positive_mod, is_legal_vector
from deletions_reconstruction import reconstruct_deletion
from insertions_reconstruction import reconstruct_insertion


class ShiftedVTCode:

    def __init__(self, n: int, c: int, d: int, P: int):
        """Initialize the encoder/decoder with the given parameters.

            Parameters:
                    n (int): the length of a word in the codespace.
                    c (int): the weighted sum of a word in the code is congruent to c (mod P).
                    d (int): the parity of the words in the codspace.
                    P (int): maximum distance of error from a known index.
        """
        self.n = n

        self.redundancy = ceil(log(P)) + 1
        self.d = d
        self.P = P
        self.c = c

    def _remove_redudancy(self, vector: List[int]):
        vector.pop(self.P - 1)

        for i in range(ceil(log(self.P)) - 1, -1, -1):
            index = (2 ** i) - 1
            vector.pop(index)

    def encode(self, vector: List[int]) -> List[int]:
        """Encodes the given word into a word in the codespace.

            Parameters:
                    vector (List[int]): the word to encode.

            Returns:
                    a word from the codeword.
        """
        if len(vector) != self.n - self.redundancy:
            raise ValueError("Invalid vector length! cannot map to a legal codeword")

        vector_copy = vector.copy()

        for i in range(ceil(log(self.P))):
            index = (2 ** i) - 1
            vector_copy.insert(index, 0)

        vector_copy.insert(self.P - 1, 0)

        wt = weighted_sum(vector_copy)
        diff = positive_mod(self.c - wt, self.P)

        for i in range(ceil(log(self.P)) - 1, -1, -1):
            index = (2 ** i) - 1
            if diff >= index + 1:
                vector_copy[index] = 1
                diff -= index + 1

        parity = sum(vector_copy) % 2

        if parity != self.d:
            vector_copy[self.P - 1] = 1

        return vector_copy

    def decode(self, vector: List[int], u: int = -1) -> List[int]:
        """Decodes the given codeword (might have deletions/insertions) to the original word.

            Parameters:
                    vector (List[int]): a word to decode to the original word.
                    u (int): the first index at which an error may have occured (upto P spaces to the right).

            Returns:
                    decoded_vector (List[int]): the original word.
        """
        if len(vector) == self.n:
            vector_copy = vector.copy()
            self._remove_redudancy(vector_copy)
            return vector_copy

        vector_copy = vector.copy()
        vector_copy.insert(0, 0)
        if len(vector) == self.n - 1:
            vector_copy = reconstruct_deletion(vector_copy, self.c, self.d, u + 1, self.P)
        elif len(vector) == self.n + 1:
            vector_copy = reconstruct_insertion(vector_copy, self.c, self.d, u + 1, self.P)
        else:
            raise ValueError("Invalid vector!")
        vector_copy.pop(0)

        self._remove_redudancy(vector_copy)
        return vector_copy
