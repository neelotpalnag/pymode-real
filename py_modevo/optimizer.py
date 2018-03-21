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
from operations.crossover_binary import cross_binary
from operations.selection import selection
from operations.elitism import elitism
from operations.evaluate import evaluate
from operations.pareto_tools import ranking


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

        # List of Objective Functions : Set in ./evaluate


        self.X_lo = [0, -5, -5, -5, -5, -5, -5, -5, -5, -5]          # List of Upper bounds of Xi's  #   Must be set by user
        self.X_hi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]          # List of Lower bounds of Xi's  #   Must be set by user

        self.crossover_prob = 0.3   # Default  = 0.3 ; Increase to 0.9 for quick convergence, or else to 0.1


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
                    X_mutated = mutate(X_parent, self.X_hi, self.X_lo, self.population_size)
                    # print(X_mutated)

                    # STEP 3: Crossover
                    X_crossed = cross_binary(X_parent, X_mutated, self.crossover_prob, self.X_hi, self.X_lo,
                                             self.population_size)
                    # print(X_crossed)

                    # STEP 4: Selection
                    X_sel = selection(self.num_objectives, X_crossed, X_parent, self.population_size)
                    # Uncomment the following lines to output daughter population values at every generation
                    # print(X_sel)

                    # STEP 5: Elitism
                    X_elite = elitism(self.num_objectives, X_parent, X_sel)
                    # print("ELITE: " + str(X_elite))

                    X_parent = X_elite[0][:self.population_size]

                print(str(self.max_generations) + " generations ended. Computing result ..")
                print(X_parent)

                # Generate file for pareto generation:
                Pareto_front = X_elite[1]
                print("Pareto front: " + str(Pareto_front))

            else:
                # Proceed with Single-Objective Optimization if um_objectives = 1
                X_evo = X_init
                for i in range(0, self.max_generations, 1):
                    # STEP 2: Mutation
                    X_mutated = mutate(X_evo, self.X_hi, self.X_lo, self.population_size)

                    # STEP 3: Crossover
                    X_crossed = cross_binary(X_evo, X_mutated, self.crossover_prob, self.X_hi, self.X_lo,
                                             self.population_size)

                    # STEP 4: Selection
                    X_evo = selection(self.num_objectives, X_crossed, X_evo, self.population_size)
                    # Uncomment the following lines to output population values at every generation
                    # print("GENERATION : " + i)
                    # print(X_evo)

                print(str(self.max_generations) + " generations ended. Computing result ..")


                print("\n \n The Optimal solution for the given objective is :")
                best_value = evaluate(X_evo[0])
                best_member_index = 0
                for solution in range(1, self.population_size, 1):
                    X = X_evo[solution]
                    this_value = evaluate(X_evo[0])
                    if this_value<best_value:
                        best_value = this_value
                        best_member_index = solution

                print("Optimal Value: " + str(best_value) + " \n Best Solution: " + str(X_evo[best_member_index]))


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


# Un-comment the following code to test:
def main():
    op = Optimizer()
    op.population_size = 50
    op.max_generations = 500
    op.num_params = 10
    op.num_objectives = 2

    # Define the objectives in the "Optimizer" class

    op.solve()

if __name__ == '__main__':
    main()