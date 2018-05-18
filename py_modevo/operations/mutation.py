import random
import math


def mutate(X, X_hi, X_lo, pop_size, seed_gen, first_vector_type = 'rand', num_difference_vectors = 1):
    # The method "mutate" requires the following parameters:
    # X : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size
    # num_difference_vectors : Number of Difference Vectors to be used


    num_vars = len(X_hi)
    X_mut = [[0 for x in range(num_vars)] for y in range(pop_size)]
    random.seed(seed_gen)
    F = 2*random.uniform(0,1)


    # NUM_DIFFERENCE_VECTORS = 1 : One Difference Vector
    # NUM_DIFFERENCE_VECTORS = 2 : Two Difference Vectors
    if num_difference_vectors == 2:
        num_rans = 5
    else:
        num_rans = 3

    # FIRST_VECTOR_TYPE : 'rand' or 'best'
    X_FIRST = []
    # if first_vector_type == 'best':
    #     X_FIRST =
    # else:
    #     pass


    if num_rans == 3:
        for i in range(0, pop_size, 1):
            for j in range(0, num_vars, 1):

                rn_int = random.sample(range(0, num_vars), num_rans)
                val = X[i][rn_int[0]] + F * (X[i][rn_int[1]] - X[i][rn_int[2]])

                if val > X_hi[j]:
                    X_mut[i][j] = X_hi[j]
                elif val < X_lo[j]:
                    X_mut[i][j] = X_lo[j]
                else:
                    X_mut[i][j] = val


    else:
        for i in range(0, pop_size, 1):
            for j in range(0, num_vars, 1):
                rn_int = rn_int = random.sample(range(0, num_vars), num_rans)

                val = X[i][rn_int[0]] + F * (X[i][rn_int[1]] - X[i][rn_int[2]]) + F * (X[i][rn_int[3]] - X[i][rn_int[4]])

                if val > X_hi[j]:
                    X_mut[i][j] = X_hi[j]
                elif val < X_lo[j]:
                    X_mut[i][j] = X_lo[j]
                else:
                    X_mut[i][j] = val

    return X_mut