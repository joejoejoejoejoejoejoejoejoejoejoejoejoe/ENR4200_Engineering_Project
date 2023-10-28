import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the CSV file
file_path = 'patient_0_test_7.csv'
data = pd.read_csv(file_path)

# Extract joint names from the first row of the CSV file
joint_names = data.columns[::3]

# Create 3D plots for each joint
for i in range(len(joint_names)):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Extract x, y, and z values for the current joint
    x_values = data[data.columns[i * 3]].dropna()
    y_values = data[data.columns[i * 3 + 1]].dropna()
    z_values = data[data.columns[i * 3 + 2]].dropna()

    # Plot 3D points
    ax.scatter(x_values, y_values, z_values, c='b', marker='o')

    # Set labels for axes
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # Set title for the plot based on joint name
    ax.set_title(f'3D Plot for {joint_names[i]}')

    # Show the plot
    plt.show()
