from itertools import product
from typing import List
from random import randrange


def gen(c, d, n, P):
    assert P > 1
    good, bad = 0,0
    for tup in product([1, 0], repeat=n):
        good += 1
        tup = list(tup)
        if is_legal_vector(tup, c, d, P):
            tup.insert(0, 0)
            start_index = randrange(1, n)
            max_error_index = min(n, start_index + P - 2)
            delete_index = randrange(start_index, max_error_index+1)
            fucked_tup = tup.copy()
            fucked_tup.pop(delete_index)
            saved_fuck_up = fucked_tup.copy()
            rec = reconstruct(fucked_tup, d, c, P, start_index, delete_index)
            if not rec == tup:
                bad +=1
                print("----")
                print(tup)
                print(saved_fuck_up)
                print(rec)
                reconstruct(saved_fuck_up, d, c, P, start_index, delete_index)
    print("ACC{}".format(1-bad/good))
def is_legal_vector(vector: List[int], c: int, d: int, P: int) -> bool:
    return weighted_sum(vector) % P == c and sum(vector) % 2 == d


def weighted_sum(vector: List[int]) -> int:
    return sum([(i+1) * x for i, x in zip(range(0, len(vector)), vector)])


def sum_mod2(vector: List[int]) -> int:
    return sum(vector) % 2


def reconstruct(vector: List[int], d: int, c: int, P: int, index: int, realIndex) -> List[int]:
    missing_value = 0 if sum_mod2(vector) == d else 1
    start = index
    #this is u + P -2 from the paper
    end = min(len(vector) - 1, index + P - 2)


    errd = vector.copy()
    errd = errd[index:end + 1]

    c_tag = (sum([i * e for i, e in enumerate(vector[:end + 1])]) + sum([((end + 1) + i + 1) * e for i, e in enumerate(vector[end + 1:])])) % P

    delta = c - c_tag
    while delta < 0:
        delta += P


    deleted_index = 0

    if missing_value == 0:
        count_ones = sum(errd)
        if count_ones == delta:
            vector.insert(index, missing_value)
            return vector
        for i in range(len(errd)):
            if count_ones == delta:
                deleted_index = i
                break
            if errd[i] == 1:
                count_ones -= 1
            if count_ones == delta:
                deleted_index = len(errd) - 1
    else:
        delta_tag = delta - index - weighted_sum(errd) % P
        while delta_tag < 0:
            delta_tag += P
        if delta_tag == 0:
            insert_place = min(index + 1, end)
            vector.insert(index, missing_value)
            if not is_legal_vector(vector, c, d, P):
                del vector[index]
                vector.insert(insert_place, missing_value)
            return vector
        count_zeros = 0
        for i in range(len(errd)):
            if count_zeros == delta_tag:
                deleted_index = i
                break
            if errd[i] == 0:
                count_zeros += 1
            if count_zeros == delta_tag:
                deleted_index = len(errd) - 1

    vector.insert(deleted_index + index, missing_value)
    return vector


if __name__ == "__main__":
    gen(c=1, d=1, n=6, P=3)
    print("done")
