# Copyright 2018 Neelotpal Nag
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from operations.initialization import initialize
from operations.mutation import mutate
from operations.crossover_binomial import cross_binomial
from operations.selection import selection
from operations.elitism import elitism

from matplotlib import pyplot as plotter


# Specify the Objective Functions in a Matrix format
# For objective function matrix F(x) = [F1(x), F2(x) ... Fk(x)], where x = [x1, x2,x3 ..., xn]
# Specify the upper & lower limits of parameter-space i.e. X_hi[] & X_lo[]

class Optimizer:

    def __init__(self):

        # Initialize all these
        self.population_size = 10   # Default = 10
        self.max_generations = 100  # Default = 100
        self.num_objectives = 1     # Must be set by user
        self.num_params = 2         # Must be set by user
        self.X = []

        self.DE_MODE = ['R', '1', 'BIN']       # Set to Rand/1/Bin by default

        # List of Objective Functions : Set in ./evaluate


        self.X_lo = []          # List of Upper bounds of Xi's  #   Must be set by user in MAIN()
        self.X_hi = []          # List of Lower bounds of Xi's  #   Must be set by user in MAIN()

        self.crossover_prob = 0.3  # Default  = 0.3 ; Increase to 0.9 for quick convergence, or else to 0.1


        if self.DE_MODE[1] == '1':
            self.num_difference_vectors = 1
        elif self.DE_MODE[1] == '2':
            self.num_difference_vectors = 2
        else:
            exit(0)



    def solve(self):
        # STEP 1: Generate the INITIAL POPULATION
        X_init = initialize(self.X_hi, self.X_lo, self.population_size)

        if self.secure_expression_check() is True:
            if self.num_objectives >= 2:
                # Proceed with multi-objective optimization only if num_objectives >=2
                X_parent = X_init
                # print(X_init)

                for i in range(0, self.max_generations, 1):
                    print("GENERATION : " + str(i))

                    # STEP 2: Mutation
                    X_mutated = mutate(X_parent, self.X_hi, self.X_lo, self.population_size, seed_gen=i, num_difference_vectors=self.num_difference_vectors)
                    # print(X_mutated)

                    # STEP 3: Crossover
                    X_crossed = cross_binomial(X_parent, X_mutated, self.crossover_prob, self.X_hi, self.X_lo,
                                             self.population_size)
                    # print(X_crossed)

                    # STEP 4: Selection
                    X_sel = selection(self.num_objectives, X_crossed, X_parent, self.population_size)
                    # Uncomment the following lines to output daughter population values at every generation
                    # print(X_sel)

                    # STEP 5: Elitism
                    ELITISM_RES = elitism(self.num_objectives, X_parent, X_sel)
                    # print("ELITE: " + str(X_elite))

                    X_parent = ELITISM_RES[0][:self.population_size]

                print(str(self.max_generations) + " generations ended. Computing result ..")
                print(X_parent)

                # Generate file for pareto generation:
                Pareto_front = ELITISM_RES[1]
                print("Pareto front: " + str(Pareto_front))

                # Print the Front / Generate Graph

                F_EVAL = ELITISM_RES[2]

                # Generate the Pareto plot for the two objectives :
                AXIS_X = [0 for t in range(0, len(Pareto_front[1]), 1)]
                AXIS_Y = [0 for t in range(0, len(Pareto_front[1]), 1)]
                res = open("zdt4.txt", 'w')

                for i in range(0, len(Pareto_front[1]), 1):
                    AXIS_X[i] = (F_EVAL[Pareto_front[1][i]][0])
                    AXIS_Y[i] = (F_EVAL[Pareto_front[1][i]][1])
                    res.write(str(AXIS_X[i]) + "," + str(AXIS_Y[i]) + "\n")

                res.close()

                # Print the Plot
                plotter.scatter(AXIS_Y, AXIS_X)
                plotter.show()


    # TODO: Eliminate or Fix
    def secure_expression_check(self):
        # safety_checklist = ["sudo", "su", "rm", "del", "dir", "dd", "mv", "git",
        #                     "wget"]
        # for i in range(0, self.num_objectives, 1):
        #     for j in safety_checklist:
        #         if j in i:
        #             print("Insecure Expression detected")
        #             print("TERMINATING")
        #             return False
        #
        # print("Secure Expressions found. Proceeding .. ")
        return True



def main():
    op = Optimizer()
    op.population_size = 100
    op.max_generations = 800
    op.num_params = 10
    op.num_objectives = 2

    # Define the objectives in the "Optimizer" class

    op.X_hi = [0, -5, -5, -5, -5, -5, -5, -5, -5, -5]          # List of Upper bounds of Xi's  #   Must be set by user
    op.X_lo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]                   # List of Lower bounds of Xi's  #   Must be set by user


    op.DE_MODE = ['R', '1', 'bin']
    op.solve()

if __name__ == '__main__':
    main()