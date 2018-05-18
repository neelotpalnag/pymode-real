import random
import math


def mutate(X, X_hi, X_lo, num_objectives, pop_size, seed_gen):
    # The method "mutate" requires the following parameters:
    # X : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    num_params = len(X_hi)
    X_mut = [[0 for x in range(num_params + num_objectives)] for y in range(pop_size)]
    random.seed(seed_gen)
    F = 2 * random.uniform(0, 1)

    for i in range(0, pop_size, 1):
        rn_int = random.sample(range(0, pop_size), 3)
        for j in range(0, num_params, 1):
            val = X[rn_int[0]][j] + F * (X[rn_int[1]][j] - X[rn_int[2]][j])
            if val > X_hi[j]:
                X_mut[i][j] = X_hi[j]
            elif val < X_lo[j]:
                X_mut[i][j] = X_lo[j]
            else:
                X_mut[i][j] = val

        for k in range(0, num_objectives, 1):
            X_mut[i][num_params+k] = 0

    return X_mut