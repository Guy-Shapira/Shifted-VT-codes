from utils import *


def reconstruct_deletion(vector: List[int], c: int, d: int, u: int, P: int) -> List[int]:
    del_val = 0 if sum_mod2(vector) == d else 1
    # this is u + P - 2 from the paper
    end = min(len(vector) - 1, u + P - 2)
    errd = vector.copy()
    errd = errd[u:end + 1]

    c_tag = (sum([i * e for i, e in enumerate(vector[:end + 1])]) + sum([((end + 1) + i + 1) * e for i, e in enumerate(vector[end + 1:])])) % P

    delta = c - c_tag
    delta = positive_mod(delta, P)

    deleted_index = end + 1

    if del_val == 0:
        count_ones = sum(errd)
        for i in range(len(errd)):
            if count_ones == delta:
                deleted_index = i + u
                break
            if errd[i] == 1:
                count_ones -= 1
    else:
        delta_tag = (delta - u - sum(errd)) % P
        delta_tag = positive_mod(delta_tag, P)

        count_zeros = 0
        for i in range(len(errd)):
            if count_zeros == delta_tag:
                deleted_index = i + u
                break
            if errd[i] == 0:
                count_zeros += 1

    vector.insert(deleted_index, del_val)
    return vector
