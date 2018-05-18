import random
import math


def cross_binomial(X, V, cr, X_hi, X_lo, pop_size):
    # The method "cross_binary" requires the following parameters:
    # X : The population from the previous generation
    # V : The mutated population
    # cr : The Crossover Probability, usually around 0.5
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    random.seed(6543)

    num_vars = len(X_hi)
    X_cross = [[0 for x in range(len(X_hi))] for y in range(pop_size)]

    for i in range(0, pop_size, 1):
        rand = math.ceil(random.random() * num_vars)
        j_rand = rand if rand!= 0 else rand+1
        for j in range(0, num_vars, 1):
            if cr > random.random() or j == j_rand:
                X_cross[i][j] = V[i][j]
            else:
                X_cross[i][j] = X[i][j]

    return X_cross
