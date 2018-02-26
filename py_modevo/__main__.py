from initialization import initialize
from mutation import mutate
from crossover_binary import cross_binary
from selection import selection

# Specify the Objective Functions in a Matrix format
# For objective function matrix F(x) = [F1(x), F2(x) ... Fk(x)], where x = [x1, x2,x3 ..., xn]
# Specify the upper & lower limits of parameter-space i.e. X_hi[] & X_lo[]


def main():
    # Parameters specific to Differential Evolution
    population_size = 4
    max_generations = 50
    num_ojectives = 1
    num_params = 1
    crossover_prob = 0.2

    X_hi = [6, 6]
    X_lo = [0, 0]

    # STEP 1: Generate the INITIAL POPULATION
    X_init = initialize(X_hi, X_lo, population_size)

    if secure_expression_check(F) is True:
        # Proceed with multi-objective optimization only if num_objectives >=2
        if num_ojectives >= 2:
            pass

        # Proceed with Single-Objective Optimization if um_objectives = 1
        else:
            X = X_init
            for i in range(0, max_generations, 1):
                # STEP 2: Mutation
                X_mutated = mutate(X, X_hi, X_lo, population_size)

                # STEP 3: Crossover
                X_Crossed = cross_binary(X, X_mutated, crossover_prob, X_hi, X_lo, population_size)

                # STEP 4: Selection
                X = selection(F, X_Crossed, X, population_size)

            print(str(max_generations) + " generations ended. Computing result ..")



def secure_expression_check(F):
    # list of safe methods
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']
    for i in F:
        for j in safe_list:
            if j in i:
                print("Insecure Expression. Please use operators only from the following list:")
                print("acos, asin, atan, atan2, ceil, cos,\n"
                 +"cosh, degrees, e, exp, fabs, floor,\n"
                 +"fmod, frexp, hypot, ldexp, log, log10,\n"
                 + "modf, pi, pow, radians, sin, sinh, sqrt,\n"
                 + "tan, tanh\n")
                print("TERMINATING..")
                return False

    print("Secure Expressions found. Proceeding .. ")
    return True
            

if __name__ == "__main__":
    main()
