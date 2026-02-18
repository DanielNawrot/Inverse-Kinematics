import matplotlib.pyplot as plt
import matplotlib.figure as figure
import matplotlib.animation as animation
import numpy as np
import compute as IK
import move_arm as MA

# Arm component lengths
L1 = 3
L2 = 3
L = 8


# Initial angles 
q1 = 0
q2 = 0            


# Get user input for start and end coordinates of X, and number of intervals for animation
# start_x = float(input("Enter start x coordinate of X: "))
# start_y = float(input("Enter start y coordinate of X: "))
# end_x = float(input("Enter end x coordinate of X: "))
# end_y = float(input("Enter end y coordinate of X: "))
# w = float(input("Enter number of rad per second: "))


# Define start and end coordinates, and angular velocity for animation
start_x = 1
start_y = 5
end_x = -1
end_y = -0.5
w = 0.7

# List to store angles at each interval for animation
y = []

# Time step for animation
dt = 0.1

# Calculate initial and target angles using inverse kinematics
q1, q2 = IK.find_angles(start_x, start_y, L1, L2, q1, q2)
q1_t, q2_t = IK.find_angles(end_x, end_y, L1, L2, q1, q2)

# Move the arm from initial to target angles, storing the angles at each interval for animation
while q1 != q1_t or q2 != q2_t:
    q1, q2 = MA.move(q1, q2, q1_t, q2_t, w, dt)
    y.append((q1, q2))


    
# Set up the figure and axis for animation
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(autoscale_on=True, xlim=(-L, L), ylim=(-L, L))
ax.set_aspect('equal')
ax.grid()
ax.plot(0, 0, 'ko', markersize=10)  # Origin point

# Define the target point and arm segments for animation
target_x, = ax.plot(end_x, end_y, 'ro', markersize=10)  # Target point X
line1, = ax.plot([], [], 'b-', linewidth=4) # First arm segment
line2, = ax.plot([], [], 'g-', linewidth=4 ) # Second arm segment

# Set labels and title
plt.title('2D Robotic Arm Configuration')
plt.xlabel('X-axis')    
plt.ylabel('Y-axis')

# Animation function to update the arm segments based on the angles at each interval
def animate(i):
    q1, q2 = y[i]

    l1x = [0, L1 * np.cos(q1)]
    l1y = [0, L1 * np.sin(q1)]
    l2x = [L1 * np.cos(q1), L1 * np.cos(q1) + L2 * np.cos(q1 + q2)]
    l2y = [L1 * np.sin(q1), L1 * np.sin(q1) + L2 * np.sin(q1 + q2)]

    line1.set_data(l1x, l1y)  # Update first arm segment
    line2.set_data(l2x, l2y)  # Update second arm segment


ani = animation.FuncAnimation(fig, animate, len(y), interval=100, repeat=False)

plt.show()