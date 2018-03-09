def selection(objF, X_trial, X_target, pop_size):
    X_sel = [[0 for x in range(len(X_trial))] for y in range(pop_size)]
    for i in range(0, pop_size, 1):
        X = X_trial
        trial_F_val = eval(objF)
        X = X_target
        target_F_val = eval(objF)
        if trial_F_val < target_F_val:
            X_sel[i] = X_trial[i]
        else:
            X_sel[i] = X_target[i]

    return X_sel