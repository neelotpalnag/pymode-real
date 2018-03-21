from math import *

def evaluate(obj_index, x_input):
    # ZDT4 Problem
    X = x_input
    F = [0, 0]

    # Objective 1
    F[0] = X[0]

    # Objective 2
    F[1] = 91
    for i in range(1, 10, 1):
        F[1] = F[1] + pow(X[i],2) - (10 * cos(4 * pi * X[i]))
    F[1] = F[1] * (1 - (X[0] / F[1]))

    return F[obj_index]