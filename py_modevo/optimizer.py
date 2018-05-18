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

from math import *
import math
from matplotlib import pyplot as plotter

global CTR
CTR = 0
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
        X_init = initialize(self.X_hi, self.X_lo, self.population_size, self.num_objectives)

        if True:
            if self.num_objectives >= 2:
                # Proceed with multi-objective optimization only if num_objectives >=2
                X_parent = X_init
                # print(X_init)

                for i in range(0, self.max_generations, 1):
                    print("GENERATION : " + str(i))

                    # STEP 2: Mutation
                    X_mutated = mutate(X_parent, self.X_hi, self.X_lo, self.num_objectives, self.population_size, seed_gen=i)
                    # print(X_mutated)

                    # STEP 3: Crossover
                    X_crossed = cross_binomial(X_parent, X_mutated, self.crossover_prob, self.X_hi, self.X_lo,
                                             self.population_size, self.num_objectives)
                    # print(X_crossed)

                    # STEP 4: Selection
                    X_sel = selection(self.num_objectives, X_crossed, X_parent, self.population_size, self.num_params)
                    # Uncomment the following lines to output daughter population values at every generation
                    # print(X_sel)

                    # STEP 5: Elitism
                    ELITISM_RES = elitism(self.num_objectives, X_parent, X_sel, self.num_params)
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
                plotter.plot(AXIS_Y, AXIS_X)
                plotter.show()

##########################################################################################################################
import random


def initialize(X_hi, X_lo, pop_size, num_objectives):
    X_init = [[0 for x in range(len(X_hi)+num_objectives)] for y in range(pop_size)]
    for i in range(0, pop_size, 1):
        for j in range(0, len(X_hi), 1):
            rn = random.uniform(0, 1)
            X_init[i][j] = round(X_lo[j] + rn * (X_hi[j] - X_lo[j]), 4)

        for k in range(0, num_objectives, 1):
            X_init[i][len(X_hi)+k] = evaluate(k, X_init[i][:len(X_hi)])

    return X_init


##########################################################################################################################

def cross_binomial(X, V, cr, X_hi, X_lo, pop_size, num_objectives):
    # The method "cross_binary" requires the following parameters:
    # X : The population from the previous generation
    # V : The mutated population
    # cr : The Crossover Probability, usually around 0.5
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    random.seed(6543)

    num_vars = len(X_hi)
    X_cross = [[0 for x in range(len(X_hi)+num_objectives)] for y in range(pop_size)]

    for i in range(0, pop_size, 1):
        random.seed(i)
        rand = math.ceil(random.random() * num_vars)
        j_rand = rand if rand!= 0 else rand+1
        for j in range(0, num_vars, 1):
            if cr > random.random() or j == j_rand:
                X_cross[i][j] = V[i][j]
            else:
                X_cross[i][j] = X[i][j]

        for k in range(0, num_objectives, 1):
            X_cross[i][num_vars+k] = 0

    return X_cross


##########################################################################################################################

# Perform
def elitism(num_obj, X_parent, X_daughter, num_params):

    X_pool = X_parent + X_daughter

    pop_size = len(X_parent)

    # STEP 1 : Create fronts of all 2 x pop_size individuals in the combined pool of parent and daughter

    # F_evaluated is a 2D list, with elements as [Objective][Individual]
    # F_evaluated[i][j] implies the value of the (i)th objective for the (j)th individual
    F_evaluated = [[0 for x in range(0, num_obj, 1)] for y in range(2*pop_size)]
    for f in range(0, num_obj, 1):
        for i in range(0, len(X_pool), 1):
            F_evaluated[i][f] = X_pool[i][num_params + f]

    [Fronts, Individuals] = ranking(F_evaluated, X_pool)


    # elite_population = [[0 for x in range(0, num_params, 1)] for y in range(pop_size)]
    elite_population = []
    counter = 2*pop_size
    for front in Fronts:
        front_size = len(Fronts[front])
        if front_size<=counter:
            counter = counter - front_size
            for i in Fronts[front]:
                elite_population.append(Individuals[i].X)

        else:
            # Sort the individuals of the current front on the basis of crowding distance
            # and select the allowed number of individuals with higher crowding distances
            sorter_dict = {}
            front_unsorted = Fronts[front]
            for i in front_unsorted:
                sorter_dict[i] = Individuals[i].crowding_distance

            buf = sorted(sorter_dict, key=sorter_dict.__getitem__, reverse=True)
            for i in range(0, counter, 1):
                elite_population.append(Individuals[buf[i]].X)

    return [elite_population[:pop_size], Fronts, F_evaluated]

##########################################################################################################################


def mutate(X, X_hi, X_lo, num_objectives, pop_size, seed_gen):
    # The method "mutate" requires the following parameters:
    # X : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    num_params = len(X_hi)
    X_mut = [[0 for x in range(num_params + num_objectives)] for y in range(pop_size)]
    random.seed(seed_gen)
    F = 2 * random.uniform(0, 1)

    for i in range(0, pop_size, 1):
        rn_int = random.sample(range(0, pop_size), 3)
        for j in range(0, num_params, 1):
            val = X[rn_int[0]][j] + F * (X[rn_int[1]][j] - X[rn_int[2]][j])
            if val > X_hi[j]:
                X_mut[i][j] = X_hi[j]
            elif val < X_lo[j]:
                X_mut[i][j] = X_lo[j]
            else:
                X_mut[i][j] = val

        for k in range(0, num_objectives, 1):
            X_mut[i][num_params+k] = 0

    return X_mut


##########################################################################################################################

from math import inf

# Input Arguments for Ranking & Crowding Distance calculation
# F : The list of objective functions
# X_in : The sample population in the form of 2D list of dimension X_in[pop_size][num_of_params]
# Rest are self-explanatory

class Individual:
    def __init__(self, idx, X, F):
        self.id = idx
        self.X = X # Coefficient matrix of the individual vector
        self.F = F # Solution Matrix of the Individual (for all objectives)

        self.sp = [] # Set of individuals dominated by this individual
        self.np = 0 # Number of individuals that dominate this individual

        self.rank = 0
        self.crowding_distance = 0

    def __repr__(self):
        return repr(())


def ranking(F, X_in):
    # F is a 2D list, with elements as [Objective][Individual]
    # F[i][j] implies the value of the (i)th objective for the (j)th individual
    front = 1
    Fronts = dict(
        [(front, [])]
    )

    num_objectives = len(F[0])
    pop_size = len(X_in)


    individuals = []
    for i in range(0, pop_size, 1):
        individuals.append(Individual(i, X_in[i], F[i]))
        individuals[i].sp = []
        individuals[i].np = 0

    for i in range(0, pop_size, 1):
        for j in range(0, pop_size, 1):
            less_d = 0
            equal_d = 0
            more_d = 0
            for k in range(0, num_objectives, 1):
                if F[i][k]>F[j][k]:
                    less_d  = less_d  + 1
                elif F[i][k] == F[j][k]:
                    equal_d = equal_d + 1
                else:
                    more_d = more_d + 1

            if (less_d==0) & (equal_d != num_objectives):
                individuals[i].sp.append(j)

            elif (more_d==0) & (equal_d != num_objectives):
                individuals[i].np = individuals[i].np + 1

        if individuals[i].np == 0:
            individuals[i].rank = 1
            Fronts[front].append(i)
            front_mem = Fronts[front]
            dat = dict(
                [(front,front_mem)]
            )
            Fronts.update(dat)

    while Fronts[front]:
        buff = []
        for i in range(0, len(Fronts[front])):
            if individuals[Fronts[front][i]].sp:
                for j in range(0,len(individuals[Fronts[front][i]].sp), 1):
                    individuals[individuals[Fronts[front][i]].sp[j]].np = \
                        individuals[individuals[Fronts[front][i]].sp[j]].np - 1

                    if individuals[individuals[Fronts[front][i]].sp[j]].np == 0:
                        individuals[individuals[Fronts[front][i]].sp[j]].rank = front +1
                        buff.append(individuals[Fronts[front][i]].sp[j])


        front  = front + 1
        Fronts[front] = buff

    individuals = crowding_distance(Fronts, individuals, num_objectives)

    return [Fronts, individuals]



def crowding_distance(fronts, individuals, num_objectives):


    for front in fronts:
        for objective in range(0, num_objectives, 1):
            front_indivs_unsorted = fronts[front]
            sorter_dict = {}
            for i in front_indivs_unsorted:
                sorter_dict[i] = individuals[i].F[objective]

            front_indivs_sorted = sorted(sorter_dict, key=sorter_dict.__getitem__, \
                                                             reverse= False)


            len_front_indiv = len(front_indivs_sorted)
            if len_front_indiv > 2:
                individuals[front_indivs_sorted[0]].crowding_distance = \
                    individuals[front_indivs_sorted[len_front_indiv-1]].crowding_distance = inf

                f_max = individuals[front_indivs_sorted[len_front_indiv - 1]].F[objective]
                f_min = individuals[front_indivs_sorted[0]].F[objective]

                for i in range(1, len_front_indiv - 1, 1):
                    prev_indiv_val = individuals[front_indivs_sorted[i - 1]].F[objective]
                    next_indiv_val = individuals[front_indivs_sorted[i + 1]].F[objective]
                    if f_max != f_min:
                        individuals[front_indivs_sorted[i]].crowding_distance = \
                            individuals[front_indivs_sorted[i]].crowding_distance + \
                            ((next_indiv_val - prev_indiv_val) / (f_max - f_min))
                    else:
                        individuals[front_indivs_sorted[i]].crowding_distance = inf


    return individuals

##########################################################################################################################

def selection(num_obj, X_trial, X_target, pop_size, num_params):

    X_sel = [[0 for x in range(num_params)] for y in range(pop_size)]
    for i in range(0, pop_size, 1):
        trial_wins = 0

        trial_F_val = []
        target_F_val = []
        for j in range(0, num_obj,1):
            trial_F_val.append(evaluate(j, X_trial[i]))
            target_F_val.append(X_target[i][num_params + j])
            if trial_F_val[j] < target_F_val[j]:
                trial_wins = 1

        if  trial_wins == 1:
            X_sel[i] = X_trial[i][:num_params] + trial_F_val

        else:
            X_sel[i] = X_target[i][:num_params] + target_F_val

    return X_sel
##########################################################################################################################

def evaluate(obj_index, x_input):
    # ZDT4 Problem
    X = x_input
    F = [0, 0]



    E = [[10, 1/10], [11, 1/12], [12, 1/15], [13, 1/20], [14, 1/25], [15, 1/35], [16, 1/40], [17, 1/42], [18, 1/43], [19, 1/48], [20, 1/52],
         [21, 1/56], [22, 1/54], [23, 1/52], [24, 1/53], [25, 1/58], [26, 1/59], [27, 1/58], [28, 1/54], [29, 1/56], [30, 1/54], [31, 1/52],
         [32, 1/54], [33, 1/55], [34, 1/56], [35, 1/58], [36, 1/59], [37, 1/60], [38, 1/62], [39, 1/63], [40, 1/64], [41, 1/64], [42, 1/62],
         [43, 1/63], [44, 1/67], [45, 1/67], [46, 1/68], [47, 1/63], [48, 1/62], [49, 1/61], [50, 1/60], [51, 1/56], [52, 1/54]]

    E_dict = {}
    for i in range(0, len(E), 1):
        E_dict[E[i][0]] = E[i][1]

    F[0] = round(X[0])
    F[1] = E_dict[round(X[0])]
    #
    # ### TODO: REPLACE WITH F[1] = GET_ACCURACY
    # F[1] = (round(X[0]))


    #
    # if obj_index==0:
    #     F[0] = X[0]
    #     return F[0]
    #
    # elif obj_index==1:
    #     global CTR
    #     CTR = CTR + 1
    #     print(CTR)
    #     F[1] = 91
    #     for i in range(1, 10, 1):
    #         F[1] = F[1] + pow(X[i], 2) - (10 * cos(4 * pi * X[i]))
    #     F[1] = F[1] * (1 - sqrt(X[0] / F[1]))
    #     return F[1]


    return F[obj_index]

##########################################################################################################################

# Un-comment the following code to test:
def main():


    op = Optimizer()
    op.population_size = 100
    op.max_generations = 2
    op.num_params = 1
    op.num_objectives = 2

    # Define the objectives in the "Optimizer" class

    op.X_hi = [52]
    op.X_lo = [10]

    op.solve()

if __name__ == '__main__':
    main()