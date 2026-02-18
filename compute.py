import numpy as np

def normalize_angle(angle):
    """Normalize angle to [-π, π] range"""
    return (angle + np.pi) % (2 * np.pi) - np.pi

def angle_difference(target, current):
    """Compute shortest angular difference from current to target"""
    return normalize_angle(target - current)

def compute_shortest_path(curr_q1, curr_q2, q2_solution, theta_X, L1, L2):
    """Find which solution gives the shortest total angular movement"""
    
    # Normalize current angles
    curr_q1_norm = normalize_angle(curr_q1)
    curr_q2_norm = normalize_angle(curr_q2)
    
    # Calculate both possible q2 values (positive and negative)
    q2_pos = q2_solution
    q2_neg = -q2_solution
    
    # Calculate corresponding q1 values
    q1_pos = theta_X - np.arctan2(L2 * np.sin(q2_pos), L1 + L2 * np.cos(q2_pos))
    q1_neg = theta_X - np.arctan2(L2 * np.sin(q2_neg), L1 + L2 * np.cos(q2_neg))
    
    # Normalize the target angles
    q1_pos_norm = normalize_angle(q1_pos)
    q1_neg_norm = normalize_angle(q1_neg)
    q2_pos_norm = normalize_angle(q2_pos)
    q2_neg_norm = normalize_angle(q2_neg)
    
    # Compute shortest angular distances for each solution
    diff_q1_pos = angle_difference(q1_pos_norm, curr_q1_norm)
    diff_q2_pos = angle_difference(q2_pos_norm, curr_q2_norm)
    diff_q1_neg = angle_difference(q1_neg_norm, curr_q1_norm)
    diff_q2_neg = angle_difference(q2_neg_norm, curr_q2_norm)
    
    # Compare total absolute angular movement
    if abs(diff_q1_pos) + abs(diff_q2_pos) <= abs(diff_q1_neg) + abs(diff_q2_neg):
        return (q1_pos_norm, q2_pos_norm)
    else:
        return (q1_neg_norm, q2_neg_norm)

def find_angles(X_x, X_y, L1, L2, curr_q1 = 0, curr_q2 = 0):
    # Distance from origin to X
    mag_x = np.sqrt(X_x**2 + X_y**2)

    # Direction from origin to X
    theta_X = np.arctan2(X_y, X_x)        

    # Angle variables, q2 is relaticve to q1.
    q1 = 0
    q2 = 0

    # Compute formula for cos(q2)
    c2 = (mag_x**2 - L1**2 - L2**2) / (2 * L1 * L2)

    # Case where X is out of reach, we will return the angles that point in the direction of X, with q2 = 0 (arm fully extended)
    if (mag_x > L1 + L2):
        return (theta_X, 0)

    # Check for existence of solution
    # If c2 is outside the range [-1, 1], then there is no solution
    if abs(c2) > 1:
        print("No solution exists for the given X and arm lengths.")
        return None
    elif c2 == 1:
        return (theta_X, 0)
    elif c2 == -1:
        if mag_x != 0:
            return (theta_X, np.pi)
        else:
            # NOTE: This case is ambiguous, since the arm could be folded in either direction, infinite solutions exist.
            return (curr_q1, np.pi)
    else:
        # NOTE: There are two solutions for q2, since cos is symmetric about the y-axis. We will return the solution with positive q2, but the other solution can be found by negating q2.
        q2 = np.arccos(c2)
        return compute_shortest_path(curr_q1, curr_q2, q2, theta_X, L1, L2)
    

   