from utils import *


def reconstruct_insertion(vector: List[int], c: int, d: int, u:int, P:int) -> List[int]:
    ins_val = 0 if sum_mod2(vector) == d else 1

    # this is u + P - 2 from the paper
    end = min(len(vector) - 1, u + P - 1)
    errd = vector.copy()
    errd = errd[u:end + 1]

    c_tag = (sum([i * e for i, e in enumerate(vector[:end + 1])]) + sum([((end + 1) + i - 1) * e for i, e in enumerate(vector[end + 1:])])) % P
    delta = c_tag - c
    delta = positive_mod(delta, P)

    to_delete_index = end + 1

    if ins_val == 0:
        count_ones = sum(errd)
        for i in range(len(errd)):
            if count_ones == delta:
                to_delete_index = i + u
                break
            if errd[i] == 1:
                count_ones -= 1
    else:
        delta_tag = (delta - u - sum(errd) + 1) % P
        delta_tag = positive_mod(delta_tag, P)

        count_zeros = 0
        for i in range(len(errd)):
            if count_zeros == delta_tag:
                to_delete_index = i + u
                break
            if errd[i] == 0:
                count_zeros += 1

    del vector[to_delete_index]
    return vector



