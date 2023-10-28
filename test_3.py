import pandas as pd

# Read the CSV file into a DataFrame with potential modifications based on inspection
try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv('dynamic_capture_01.csv', skiprows=31, header=None, usecols=range(119, 248))

    # Extract specific rows (32 to 38)
    df = df.iloc[1:8, :]  # Rows in Python are 0-based index, so row 32 corresponds to index 1

    # Find the maximum length in each column
    max_lengths = df.apply(lambda x: x.map(lambda x: len(str(x))).max())

    # Pad values in each column to match the maximum length
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).ljust(max_lengths[column]))

    # Write the extracted data to a new CSV file
    df.to_csv('patient_0_test_3.csv', index=False)

    print("Data extracted and saved to 'patient_0_test_output.csv' successfully.")

except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)

    #variable columns but not outputting them
