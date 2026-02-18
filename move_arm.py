import numpy as np


def move(q1, q2, q1_t, q2_t, w, dt):
    max_angle_change = w * dt
    diff_1 = q1_t - q1

    if diff_1 < max_angle_change and diff_1 > -max_angle_change:
        q1_next = q1_t
    elif diff_1 > 0:
        q1_next = q1 + max_angle_change
    else:
        q1_next = q1 - max_angle_change

    diff_2 = q2_t - q2
    if diff_2 < max_angle_change and diff_2 > -max_angle_change:
        q2_next = q2_t
    elif diff_2 > 0:
        q2_next = q2 + max_angle_change
    else:
        q2_next = q2 - max_angle_change  

    return (q1_next, q2_next)