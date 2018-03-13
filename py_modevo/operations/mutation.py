import random
import math


def mutate(X, X_hi, X_lo, pop_size):
    # The method "mutate" requires the following parameters:
    # X : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    F = random.uniform(0, 1)
    num_vars = len(X_hi)
    X_mut = [[0 for x in range(num_vars)] for y in range(pop_size)]

    for i in range(0, pop_size, 1):
        for j in range(0, num_vars, 1):
            rn_int = get_distinct_rn_int(num_vars)
            val = X[i][rn_int[0]] + F * (X[i][rn_int[1]] - X[i][rn_int[2]])
            if val > X_hi[j]:
                X_mut[i][j] = X_hi[j]
            elif val < X_lo[j]:
                X_mut[i][j] = X_lo[j]
            else:
                X_mut[i][j] = val

    return X_mut


def get_distinct_rn_int(cap):
    rn1 = math.ceil(random.uniform(0, 1) * cap)
    if rn1 == 0:
        rn1 = rn1 + 1
    rn2 = cap
    while rn2 != rn1:
        rn2 = math.ceil(random.uniform(0, 1) * cap)
        if rn2 == 0:
            rn2 = rn2 + 1
    rn3 = cap
    while rn3!=rn1 & rn3!=rn2:
        rn3 = math.ceil(random.uniform(0, 1) * cap)
        if rn3 == 0:
            rn3 = rn3 + 1

    return [rn1-1, rn2-1, rn3-1]