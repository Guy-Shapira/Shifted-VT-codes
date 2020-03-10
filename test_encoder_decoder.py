import unittest
from itertools import product
from utils import is_legal_vector
from random import randrange
from math import ceil, log2 as log
import ShiftedVTCode

n = 18
c = 6
d = 1
P = 15


class TestShiftedVTCodes(unittest.TestCase):

    def setUp(self):
        self.vtcode = ShiftedVTCode.ShiftedVTCode(n, c, d, P)

    def test_encode_decode(self):

        word_len = n - (ceil(log(P)) + 1)

        for vector in product([1, 0], repeat=word_len):
            vector = list(vector)

            encoded = self.vtcode.encode(vector)
            self.assertTrue(is_legal_vector(encoded, c, d, P), '\nvector: {}\nencoded: {}'.format(vector, encoded))
            reconstructed = self.vtcode.decode(encoded)
            self.assertTrue(vector == reconstructed, 'No error inserted!\nvector: {}\nencoded: {}\nreconstructed: {}'.format(vector, encoded, reconstructed))

            for start_index in range(0, n):
                    max_error_index = min(n, start_index + P - 2)
                    insertion_index = randrange(start_index, max_error_index+1)
                    original_encoded = encoded.copy()
                    insert_value = randrange(0, 2)
                    encoded.insert(insertion_index, insert_value)
                    reconstructed = self.vtcode.decode(encoded, start_index)
                    self.assertTrue(reconstructed == vector, 'Insertion error!\nvector: {}\nencoded: {}\nreconstructed: {}'.format(vector, encoded, reconstructed))
                    encoded = original_encoded
            

            for start_index in range(0, n - 1):
                    max_error_index = min(n - 1, start_index + P - 2)
                    deletion_index = randrange(start_index, max_error_index + 1)
                    original_encoded = encoded.copy()
                    encoded.pop(deletion_index)
                    reconstructed = self.vtcode.decode(encoded, start_index)
                    self.assertTrue(reconstructed == vector, 'Deletion error!\nvector: {}\nencoded: {}\nreconstructed: {}'.format(vector, encoded, reconstructed))
                    encoded = original_encoded
