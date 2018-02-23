import random
import math


def cross_binary(X, V, cr, X_hi, X_lo, pop_size):
    # The method "cross_binary" requires the following parameters:
    # X : The population from the previous generation
    # V : The mutated population
    # cr : The Crossover Probability, usually around 0.5
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    num_vars = len(X_hi)
    X_cros = [[0 for x in range(len(X_hi))] for y in range(pop_size)]

    for i in range(0, pop_size, 1):
        j_rand = math.ceil(random.uniform(0, 1) * num_vars) if j_rand != 0 else math.ceil(
            random.uniform(0, 1) * num_vars) + 1
        for j in range(0, num_vars, 1):
            if cr > random.uniform(0, 1) or j == j_rand:
                X_cros[i][j] = V[i][j]
            else:
                X_cros[i][j] = X[i][j]

    return X_cros
