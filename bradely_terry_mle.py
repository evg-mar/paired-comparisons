# -*- coding: utf-8 -*-
"""

@author: emarinov
"""


import numpy as np

team_scores = np.asarray([[0,    28,     15,     23],
                         [112,  0,      46,     47],
                         [39,   17,     0,      0],
                         [34,   11,     0,      0]])

initial_estimators = [1.0 / len(team_scores)]* len(team_scores)

# Compute paired comparisons through Maximul Liklelihood Estimation
def compute_mle(initial_estimators = initial_estimators,
                team_scores = team_scores,
                epsilon = 0.001):

    team_wins = [sum(scores) for scores in team_scores]

    sum_matrix = np.zeros(shape=(len(team_scores), len(team_scores)))
    
    for i in range(len(team_scores)):
        for j in range(len(team_scores)):
            sum_matrix[i][j] = team_scores[i][j] + team_scores[j][i]

        
    estimators = initial_estimators
    estimators_new = np.zeros_like(estimators)

    err = epsilon + 1.0
    while err > epsilon:
        print(estimators)
        for idx, estimator in enumerate(estimators):
            denum = sum( sum_matrix[idx][j] / (estimators[idx] + estimators[j]) \
                         for j in range(len(estimators)) if j!=idx)
            estimators_new[idx] = team_wins[idx] / denum 
        estimators_new = estimators_new / np.sum(estimators_new)
        err = np.max(np.abs(estimators_new - estimators))
        print(err)
        estimators = estimators_new
    
    return estimators
        
if __name__ == "__main__":
    estimators = compute_mle(initial_estimators,
                             team_scores,
                             epsilon = 0.00001)
