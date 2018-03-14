from .pareto_tools import *

# Perform
def elitism(F, X_parent, X_daughter):

    X_pool = X_parent + X_daughter

    num_params = len(X_parent[0])
    pop_size = len(X_parent)

    # STEP 1 : Create fronts of all 2 x pop_size individuals in the combined pool of parent and daughter
    F_evaluated = []
    for i in range(0, len(X_pool), 1):
        X = X_pool
        F_evaluated[i] = eval(X[i])

    [Fronts, Individuals] = ranking(F_evaluated, X_pool)

    elite_population = [[0 for x in range(0, num_params, 1)] for y in range(pop_size)]
    counter = pop_size
    for front in Fronts:
        front_size = len(Fronts[front])
        if front_size<=counter:
            counter = counter - front_size
            for i in Fronts[front]:
                elite_population.append(Individuals[i].X)

        else:
            # Sort the individuals of the current front on the basis of crowding distance
            # and select the allowed number of individuals with higher crowding distances
            buf = Fronts[front].sort(key=Individuals[Fronts[front]].crowding_distance, \
                                     reverse=True)
            for i in range(0, counter, 1):
                elite_population.append(Individuals[buf[i]].X)

            return elite_population









