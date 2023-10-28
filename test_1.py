import pandas as pd

# Open the CSV file and inspect its structure
with open('dynamic_capture_01.csv', 'r') as file:
    for line in file:
        print(line)

# Read the CSV file into a DataFrame with potential modifications based on inspection
try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv('dynamic_capture_01.csv', skiprows=31, header=None, usecols=range(119, 248))

    # Drop columns where all values are NaN (empty cells)
    df = df.dropna(axis=1, how='all')

    # Now, df contains the data you want to manipulate
    print(df)

    # Write the extracted data to a new CSV file
    df.to_csv('patient_0_test_1.csv', index=False)

    print("Data extracted and saved to 'patient_0_test_output.csv' successfully.")

except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)
