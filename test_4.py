import pandas as pd

# Read the CSV file into a DataFrame with potential modifications based on inspection
try:
    # Read the CSV file into a DataFrame              #change to 28 to get the x,y,z and under the mm
    df = pd.read_csv('dynamic_capture_01.csv', skiprows=30, header=None, usecols=range(119, 248))

    # Extract specific rows (from 32nd row to the end of the DataFrame)
    df = df.iloc[1:, :]  # Rows in Python are 0-based index, so row 32 corresponds to index 1

    # Find the maximum length in each column
    max_lengths = df.apply(lambda x: x.map(lambda x: len(str(x))).max())

    # Pad values in each column to match the maximum length
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).ljust(max_lengths[column]))

    # Write the extracted data to a new CSV file
    df.to_csv('patient_0_test_4.csv', index=False)

    print("Data extracted and saved to 'patient_0_test_output.csv' successfully.")

except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)

#variable length working well and can adjust if want to see x,y,z and under it mm as well
