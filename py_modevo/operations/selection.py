def selection(objF, X_trial, X_target, pop_size):
    X_sel = [[0 for x in range(len(X_trial[0]))] for y in range(pop_size)]
    for i in range(0, pop_size, 1):
        trial_wins = 0
        for j in range(0, len(objF),1):
            X = X_trial
            trial_F_val = eval(objF[j])
            X = X_target
            target_F_val = eval(objF[j])
            if trial_F_val < target_F_val:
                trial_wins = 1

        if  trial_wins == 1:
            X_sel[i] = X_trial[i]

        else:
            X_sel[i] = X_target[i]

    return X_sel