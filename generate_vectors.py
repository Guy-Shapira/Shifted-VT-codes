from itertools import product
from typing import List
from random import randrange


def gen(c, d, n, P):
    assert P > 1
    for tup in product([1, 0], repeat=n):
        tup = list(tup)
        if is_legal_vector(tup, c, d, P):
            # print(tup)
            start_index = randrange(n)
            max_error_index = min(n-1, start_index + P - 2)
            delete_index = randrange(start_index, max_error_index+1)
            fucked_tup = tup.copy()
            fucked_tup.pop(delete_index)
            saved_fuck_up = fucked_tup.copy()
            rec = reconstruct(fucked_tup, d, c, P, start_index, delete_index)
            if not rec == tup:
                print("----")
                print(tup)
                print(rec)
                reconstruct(saved_fuck_up, d, c, P, start_index, delete_index)
            # for i in range(start_index, end_index + 1):
            #     rec = reconstruct(fucked_tup, d, c, P, i, index)
            #     # print(rec)
            #     if rec != tup:
            #         print("----")
            #         print(tup)
            #         print(rec)
            #         reconstruct(saved_fuck_up, d, c, P, i, index)
            #     fucked_tup.pop(index)
            #     saved_fuck_up = fucked_tup.copy()


def is_legal_vector(vector: List[int], c: int, d: int, P: int) -> bool:
    return weighted_sum(vector) % P == c and sum(vector) % 2 == d


def weighted_sum(vector: List[int]) -> int:
    return sum([(i+1) * x for i, x in zip(range(0, len(vector)), vector)])


def sum_mod2(vector: List[int]) -> int:
    return sum(vector) % 2


def reconstruct(vector: List[int], d: int, c: int, P: int, index: int, realIndex) -> List[int]:
    missing_value = 0 if sum_mod2(vector) == d else 1
    #start = max(0, index - P + 2)
    start = index
    end = min(len(vector), index + P - 1)
    assert start <= realIndex <= end

    for i in range(start, end + 1):
        vector.insert(i, missing_value)
        if is_legal_vector(vector, c, d, P):
            return vector

        del vector[i]

    return None

if __name__ == "__main__":
    gen(c=6, d=1, n=18, P=15)
