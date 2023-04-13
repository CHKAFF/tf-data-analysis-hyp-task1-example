import numpy as np

from scipy.stats import norm

chat_id = 303247798

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    conv_ctrl = x_success / x_cnt
    conv_test = y_success / y_cnt

    # стандартное отклонение для данных контрольной группы
    std_ctrl = (conv_ctrl * (1 - conv_ctrl) / y_cnt) ** 0.5

    z = (conv_test - conv_ctrl) / std_ctrl
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return p_value < 0.05
