import sys
import random
import math
import cmath
from . import initialization


def main():

    # Parameters specific to Differential Evolution
    population_size = 0
    max_generations = 0
    num_ojectives = 0
    num_params = 0

    X_hi = []
    X_lo = []

    # Specify the Objective Functions in a Matrix format
    # For objective function matrix F(x) = [F1(x), F2(x) ... Fk(x)], where x = [x1, x2,x3 ..., xn]
    # F[0] = x[0] + x[1]
    # F[1] = x[0] - x[1]

    X_init = initialization(X_hi, X_lo, population_size)



if __name__ == "__main__":
    main()