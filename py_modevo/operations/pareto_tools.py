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


def ranking(F, X_in, num_params, num_objectives, pop_size):

    front =1
    Fronts = dict(
        front = []
    )

    individual = []
    for i in range(0, pop_size, 1):
        individual[i].append(Individual(i, X_in[i], F[i]))
        individual[i].sp = []
        individual[i].np = 0
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
                individual[i].np = individual[i].np +1
            elif more_d == 0 & equal_d != num_objectives:
                individual[i].sp.append(j)

        if individual[i].np == 0:
            individual[i].rank = 1
            front_mem = Fronts[front].append(i)
            dat = dict(
                front = front_mem
            )
            Fronts.update(dat)

    while Fronts[front]:
        buf = []
        for i in range(0, len(Fronts[front])):
            if individual[Fronts[front][i].sp]:
                for j in range(0,len(individual[Fronts[front][i]].sp), 1):
                    individual[individual[Fronts[front][i]].sp[j]].np = \
                        individual[individual[Fronts[front][i]].sp[j]].np - 1
                    if individual[individual[Fronts[front][i]].sp[j]].np == 0:
                        individual[individual[Fronts[front][i]].sp[j]].rank = front +1
                        buf.append[individual[Fronts[front][i]].sp[j]]

        front  = front + 1
        Fronts[front].update(buf)

    # [######]


# def crowding_distance(Fronts):
#      for front in range(0, len(Fronts) - 1, 1):
#          dist = 0;

