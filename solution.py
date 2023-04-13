import numpy as np
from scipy.stats import binom_test

from scipy.stats import norm

chat_id = 303247798

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    conv_ctrl = x_success / x_cnt
    conv_test = y_success / y_cnt

    # standard deviation of the test group
    std_dev_test = (conv_test * (1 - conv_test) / y_cnt) ** 0.5

    # z-score calculation
    z_score = (conv_test - conv_ctrl) / std_dev_test

    # significance level
    alpha = 0.05

    # critical z-value
    z_crit = norm.ppf(alpha)

    return z_score < z_crit
