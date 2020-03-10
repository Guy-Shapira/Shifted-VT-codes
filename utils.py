from itertools import product
from typing import List
from random import randrange

# def gen(c, d, n, P):
#     assert P > 1
#     for tup in product([1, 0], repeat=n):
#         tup = list(tup)
#         if is_legal_vector(tup, c, d, P):
#             tup.insert(0, 0)
#             start_index = randrange(1, n)
#             max_error_index = min(n, start_index + P - 2)
#             delete_index = randrange(start_index, max_error_index+1)
#             fucked_tup = tup.copy()
#             value = randrange(0, 2)
#             fucked_tup.insert(delete_index, value)
#             saved_fuck_up = fucked_tup.copy()
#             rec = reconstruct_insertion(fucked_tup, c, d, start_index, P)
#             if not rec == tup:
#                 print("----")
#                 print(tup)
#                 print(saved_fuck_up)
#                 print(rec)
#                 rec = reconstruct_insertion(fucked_tup, c, d, start_index, P)


def is_legal_vector(vector: List[int], c: int, d: int, P: int) -> bool:
    return weighted_sum(vector) % P == c and sum(vector) % 2 == d


def weighted_sum(vector: List[int]) -> int:
    return sum([(i+1) * x for i, x in zip(range(0, len(vector)), vector)])


def sum_mod2(vector: List[int]) -> int:
    return sum(vector) % 2


def positive_mod(value:int, mod:int) -> int:
    while value < 0:
        value += mod
    return value
