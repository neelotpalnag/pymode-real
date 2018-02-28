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

from .operations.initialization import initialize
from .operations.mutation import mutate
from .operations.crossover_binary import cross_binary
from .operations.selection import selection

# Specify the Objective Functions in a Matrix format
# For objective function matrix F(x) = [F1(x), F2(x) ... Fk(x)], where x = [x1, x2,x3 ..., xn]
# Specify the upper & lower limits of parameter-space i.e. X_hi[] & X_lo[]

class Optimizer:

    def __init__(self):

        # Initialize all these
        self.population_size = 10   # Default = 10
        self.max_generations = 100  # Default = 100
        self.num_objectives = 0     # Must be set by user
        self.num_params = 0         # Must be set by user

        self.F = [" "]              # Must be set by user
        self.X_hi = [0, 0]          # Must be set by user
        self.X_lo = [0, 0]          # Must be set by user

        self.crossover_prob = 0.3   # Default  = 0.3 ; Increase to 0.9 for quick convergence, or else to 0.1


    def solve(self):
        # STEP 1: Generate the INITIAL POPULATION
        X_init = initialize(self.X_hi, self.X_lo, self.population_size)

        if self.secure_expression_check(self.F) is True:
            if self.num_ojectives >= 2:
                # Proceed with multi-objective optimization only if num_objectives >=2
                pass

            else:
                # Proceed with Single-Objective Optimization if um_objectives = 1
                X_evo = X_init
                for i in range(0, self.max_generations, 1):
                    # STEP 2: Mutation
                    X_mutated = mutate(X_evo, self.X_hi, self.X_lo, self.population_size)

                    # STEP 3: Crossover
                    X_Crossed = cross_binary(X_evo, X_mutated, self.crossover_prob, self.X_hi, self.X_lo, self.population_size)

                    # STEP 4: Selection
                    X_evo = selection(self.F, X_Crossed, X_evo, self.population_size)

                print(str(self.max_generations) + " generations ended. Computing result ..")
                print(X_evo)


    def secure_expression_check(self):
        # list of safe methods
        safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                     'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                     'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                     'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                     'tan', 'tanh']
        for i in self.F:
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
