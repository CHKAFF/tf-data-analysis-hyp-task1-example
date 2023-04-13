import numpy as np
from scipy.stats import binom_test

chat_id = 303247798

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    control_conversion = x_success / x_cnt
    test_conversion = y_success / y_cnt

    p_value = binom_test(y_success, y_cnt, control_conversion)

    return p_value < 0.05
