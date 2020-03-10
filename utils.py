from itertools import product
from typing import List
from random import randrange


def is_legal_vector(vector: List[int], c: int, d: int, P: int) -> bool:
    return weighted_sum(vector) % P == c and sum(vector) % 2 == d


def weighted_sum(vector: List[int]) -> int:
    return sum([(i + 1) * x for i, x in enumerate(vector)])


def sum_mod2(vector: List[int]) -> int:
    return sum(vector) % 2


def positive_mod(value: int, mod: int) -> int:
    while value < 0:
        value += mod
    return value
