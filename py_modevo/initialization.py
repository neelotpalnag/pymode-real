# For initial population generation
# Input Arguments :
# 1. The X_high & X_low matrices
# 2. Population Size

# Return Value: X_init (Initial population matrix)


import random


def initialization(X_hi, X_lo, pop_size):
    X_init = [[] * len(X_hi) for x in range(pop_size)]
    for i in range(0, pop_size, 1):
        for j in range(0, len(X_hi), 1):
            rn = random.uniform(0, 1)
            X_init[j][i] = X_lo[j] + rn * (X_hi[j] - X_lo[j])

    return X_init
