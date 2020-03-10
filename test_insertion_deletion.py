from itertools import product
from typing import List
from random import randrange
from insertions_reconstruction import reconstruct_insertion
from deletions_reconstruction import reconstruct_deletion
from utils import is_legal_vector
import unittest


n = 18
c = 6
d = 1
P = 15


class TestInsertions(unittest.TestCase):
    
    def test_insertions(self):
        for vector in product([1, 0], repeat=n):
            vector = list(vector)

            if is_legal_vector(vector, c, d, P):
                vector.insert(0, 0) # fix indices, so the indices are 1 based
                for start_index in range(1, n):
                    max_error_index = min(n, start_index + P - 2)
                    insertion_index = randrange(start_index, max_error_index+1)
                    original_vector = vector.copy()
                    insert_value = randrange(0, 2)
                    vector.insert(insertion_index, insert_value)
                    reconstructed = reconstruct_insertion(vector, c, d, start_index, P)
                    self.assertTrue(reconstructed == original_vector)

                    vector = original_vector # reset the vector for the next insertion


class TestDeletions(unittest.TestCase):

    def test_deletions(self):
        for vector in product([1, 0], repeat=n):
            vector = list(vector)

            if is_legal_vector(vector, c, d, P):
                vector.insert(0, 0) # fix indices, so the indices are 1 based
                for start_index in range(1, n):
                    max_error_index = min(n, start_index + P - 2)
                    deletion_index = randrange(start_index, max_error_index + 1)
                    original_vector = vector.copy()
                    vector.pop(deletion_index)
                    reconstructed = reconstruct_deletion(vector, c, d, start_index, P)
                    self.assertTrue(reconstructed == original_vector)

                    vector = original_vector
