from math import inf

# Input Arguements for Ranking & Crowding Distance calculation
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

        self.rank = -1
        self.crowding_distance = 0


def ranking(F, X_in, num_params, num_objectives, pop_size):

    front = 1
    Fronts = dict(
        [(front, [])]
    )

    individuals = []
    for i in range(0, pop_size, 1):
        individuals[i].append(Individual(i, X_in[i], F[i]))
        individuals[i].sp = []
        individuals[i].np = 0
        for j in range(0, pop_size, 1):
            less_d = 0
            equal_d = 0
            more_d = 0
            for k in range(0, num_objectives, 1):
                if F[i]<F[j]:
                    less_d  = less_d  + 1
                elif F[i] == F[j]:
                    equal_d = equal_d + 1
                else:
                    more_d = more_d + 1
            if less_d  == 0 & equal_d != num_objectives:
                individuals[i].np = individuals[i].np +1
            elif more_d == 0 & equal_d != num_objectives:
                individuals[i].sp.append(j)

        if individuals[i].np == 0:
            individuals[i].rank = 1
            front_mem = Fronts[front].append(i)
            dat = dict(
                [(front,front_mem)]
            )
            Fronts.update(dat)

    while Fronts[front]:
        buf = []
        for i in range(0, len(Fronts[front])):
            if individuals[Fronts[front][i].sp]:
                for j in range(0,len(individuals[Fronts[front][i]].sp), 1):
                    individuals[individuals[Fronts[front][i]].sp[j]].np = \
                        individuals[individuals[Fronts[front][i]].sp[j]].np - 1

                    if individuals[individuals[Fronts[front][i]].sp[j]].np == 0:
                        individuals[individuals[Fronts[front][i]].sp[j]].rank = front +1
                        buf.append[individuals[Fronts[front][i]].sp[j]]

        front  = front + 1
        Fronts[front].update(buf)

        return [Fronts, individuals]



def crowding_distance(fronts, individuals, num_objectives):


    for front in fronts:
        for objective in range(0, num_objectives, 1):
            front_indivs_unsorted = fronts[front]
            front_indivs_sorted = front_indivs_unsorted.sort(key=individuals[fronts[front]].F[objective], \
                                                             reverse= False)

            len_front_indiv = len(front_indivs_sorted)
            individuals[front_indivs_sorted[0]] = \
                individuals[front_indivs_sorted[len_front_indiv-1]].crowding_distance = inf

            f_max = individuals[front_indivs_sorted[len_front_indiv]-1].F[objective]
            f_min = individuals[front_indivs_sorted[0]].F[objective]

            for i in range(1, len_front_indiv-1, 1):
                prev_indiv_val = individuals[front_indivs_sorted[i-1]].F[objective]
                next_indiv_val = individuals[front_indivs_sorted[i+1]].F[objective]
                individuals[front_indivs_sorted[i]].crowding_distance = \
                    individuals[front_indivs_sorted[i]].crowding_distance + \
                    ((next_indiv_val - prev_indiv_val)/(f_max-f_min))

    return individuals