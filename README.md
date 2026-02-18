# Inverse Kinematics
In this project I tackled the first step in learning how to apply Inverse Kinematics. In a simple 2D simulation through matplotlib, I was able to implement the Inverse Kinematics algorthm for a robotic arm in 2D.

The algorithm is based on a few fundamental steps, assuming that the robotic arm has two arm members and two joints, allowing for two variable angles. 
This is shown in the picture bellow; the red dot indicates the 'target position' and the black dot indicates the origin, or arm base. 

<img width="677" height="689" alt="image" src="https://github.com/user-attachments/assets/3ea3a4fb-ad50-41d4-9db3-d99122c0b372" />

<img width="352" height="264" alt="image" src="https://github.com/user-attachments/assets/8ad277bf-50ce-4c14-9d45-db5105d208d2" />


The algorithm takes the input arguments: 
- L1
- L2
- q1
- q2

Through a series of derivations, we can compute the target angle for joint 2 (q2). 
The result then needs to be tested for ambiguous cases where there is either no solution, multiple solutions, or infinite solutions. 
Computing the primary joint angle (q1) then becomes very easy and we are left with the target joint angles to achieve the desired end position.

<img width="559" height="482" alt="image" src="https://github.com/user-attachments/assets/a40d79a8-f230-4556-9709-e1ac240ccbd5" />

