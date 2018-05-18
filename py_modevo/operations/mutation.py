import random
import math


def mutate(X, X_hi, X_lo, pop_size, seed_gen):
    # The method "mutate" requires the following parameters:
    # X : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size


    num_vars = len(X_hi)
    X_mut = [[0 for x in range(num_vars)] for y in range(pop_size)]
    random.seed(seed_gen)
    F = 2*random.uniform(0,1)

    for i in range(0, pop_size, 1):
        for j in range(0, num_vars, 1):
            rn_int = rn_int = random.sample(range(0, num_vars), 3)
            val = X[i][rn_int[0]] + F * (X[i][rn_int[1]] - X[i][rn_int[2]])
            if val > X_hi[j]:
                X_mut[i][j] = X_hi[j]
            elif val < X_lo[j]:
                X_mut[i][j] = X_lo[j]
            else:
                X_mut[i][j] = val

    return X_mut