import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from mpl_toolkits.mplot3d import Axes3D

###data preprocessing### empty cells where there is no data and should be variable length acceptable
try:# Read the CSV file into a DataFrame with potential modifications based on inspection
    df = pd.read_csv('dynamic_capture_02.csv', skiprows=28, usecols=range(119, 248))# Read the CSV file into a DataFrame, including rows 29, 30, and 31

    df = df.iloc[2:, :]# Extract specific rows (from 32nd row to the end of the DataFrame) Rows in Python are 0-based index, so row 32 corresponds to index 2

    df = df.replace({pd.NA: ''})# Replace NaN values with blank cells

    max_lengths = df.apply(lambda x: x.map(lambda x: len(str(x))).max())# Find the maximum length in each column

    for column in df.columns:# Pad values in each column to match the maximum length
        df[column] = df[column].apply(lambda x: str(x).ljust(max_lengths[column]))
    # end of for loop

    df = df.apply(pd.to_numeric, errors='coerce')# Convert columns to numeric type (assuming they are numeric)
    df = df.dropna()# Drop rows with NaN values

    df.to_csv('patient_0_test_9.csv', index=False)# Write the extracted data to a new CSV file

    print("Data extracted and saved to 'patient_0_test_9.csv' successfully.")
# end of try statemement
except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)# print out error message
# end of except statement

###plotting### uncomment for straight lines of smooth lines connecting points
data = pd.read_csv('patient_0_test_9.csv')# Read the CSV file

joint_names = data.columns[::3]# Extract joint names from the first row of the CSV file

for i in range(len(joint_names)):# Create 3D plots for each joint
    #If you want to be able to toggle "dark mode" uncomment the below
    #plt.style.use('dark_background')# dark background plots

    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(111, projection='3d')

    x_values = data[data.columns[i * 3]].dropna()# Extract x, y, and z values for the current joint
    y_values = data[data.columns[i * 3 + 1]].dropna()
    z_values = data[data.columns[i * 3 + 2]].dropna()

    ax.scatter(x_values, y_values, z_values, c='#F53AAA', marker='s', label='Points')# Plot 3D points

    #If you want to connect the points with straight lines uncomment the below:
    #ax.plot(x_values, y_values, z_values, c='r', label='Lines')# Connect points with lines

    #If you want smooth lines between the points uncomment the below:
    #tck, u = splprep([x_values, y_values, z_values], s=0)# Perform spline interpolation
    #new_points = splev(np.linspace(0, 1, 100), tck)
    #ax.plot(new_points[0], new_points[1], new_points[2], c='#3AF591', label='Smooth Curve')# Plot smooth curve

    ax.set_xlabel('X position (mm)')# Set labels for axes
    ax.set_ylabel('Y position (mm)')
    ax.set_zlabel('Z position (mm)')

    ax.set_title(f'3D Plot for: {joint_names[i]}')# Set title for the plot based on joint name

    min_x, max_x = min(x_values), max(x_values)# Set axis limits dynamically based on data
    min_y, max_y = min(y_values), max(y_values)
    min_z, max_z = min(z_values), max(z_values)

    ax.set_xlim(min_x, max_x)# fixing axis limits
    ax.set_ylim(min_y, max_y)
    ax.set_zlim(min_z, max_z)

    #ax.set_facecolor('#2F2F39')# sets the background greyish
    plt.show()# Show the plot
# end of for loop
# plots 3d scatter plots for the joints each with their own plot
