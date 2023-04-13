import numpy as np
import math

from scipy.stats import norm

chat_id = 303247798

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    control_conv = x_success / x_cnt
    test_conv = y_success / y_cnt

    # calculate total conversion rate and pooled standard error
    total_sales = x_success + y_success
    total_clicks = x_cnt + y_cnt
    total_conv = total_sales / total_clicks
    SE = math.sqrt(total_conv * (1 - total_conv) * (1/x_cnt + 1/y_cnt))

    # calculate z-score and p-value
    z_score = (control_conv - test_conv) / SE
    p_val = norm.sf(abs(z_score)) * 2

    # return True if we can reject null hypothesis
    return p_val < 0.05
