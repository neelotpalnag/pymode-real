from operations.evaluate import evaluate

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