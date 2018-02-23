from initialization import initialize


def main():
    # Parameters specific to Differential Evolution
    population_size = 4
    max_generations = 0
    num_ojectives = 0
    num_params = 0

    X_hi = [6, 6]
    X_lo = [0, 0]

    # Specify the Objective Functions in a Matrix format
    # For objective function matrix F(x) = [F1(x), F2(x) ... Fk(x)], where x = [x1, x2,x3 ..., xn]
    # F[0] = x[0] + x[1]
    # F[1] = x[0] - x[1]

    X_init = initialize(X_hi, X_lo, population_size)
    print(X_init)


if __name__ == "__main__":
    main()
