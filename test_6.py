import pandas as pd
import matplotlib.pyplot as plt

try:
    # Read the CSV file with skipping rows until you reach the valid data
    df = pd.read_csv('dynamic_capture_01.csv', skiprows=28, usecols=range(119, 248), header=None)

    # Drop empty rows
    df = df.dropna(how='all')

    # Convert x, y, z columns to numeric, handling errors and coerce empty cells to NaN
    df.iloc[:, 0::3] = df.iloc[:, 0::3].apply(pd.to_numeric, errors='coerce')
    df.iloc[:, 1::3] = df.iloc[:, 1::3].apply(pd.to_numeric, errors='coerce')
    df.iloc[:, 2::3] = df.iloc[:, 2::3].apply(pd.to_numeric, errors='coerce')

    # Write the cleaned data to a new CSV file
    df.to_csv('patient_0_test_6_cleaned.csv', index=False)

    print("Data extracted and saved to 'patient_0_test_6_cleaned.csv' successfully.")

    # Transpose the data for easier joint label plotting
    df = df.transpose()

    # Loop through columns (each joint label) and plot x, y, z in separate subplots
    for column in df.columns:
        plt.figure(figsize=(6, 4))
        plt.plot(df[column][0::3], label='x')
        plt.plot(df[column][1::3], label='y')
        plt.plot(df[column][2::3], label='z')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title(f'Joint Label: {column}')
        plt.legend()
        plt.tight_layout()
        plt.show()

except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)

#partly working graphs but weird .csv
