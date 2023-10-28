import pandas as pd

# Read the CSV file into a DataFrame with potential modifications based on inspection
try:
    # Read the CSV file into a DataFrame, including rows 29, 30, and 31
    df = pd.read_csv('dynamic_capture_02.csv', skiprows=28, usecols=range(119, 248))

    # Extract specific rows (from 32nd row to the end of the DataFrame)
    df = df.iloc[2:, :]  # Rows in Python are 0-based index, so row 32 corresponds to index 2

    # Replace NaN values with blank cells
    df = df.replace({pd.NA: ''})

    # Find the maximum length in each column
    max_lengths = df.apply(lambda x: x.map(lambda x: len(str(x))).max())

    # Pad values in each column to match the maximum length
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).ljust(max_lengths[column]))

    # Write the extracted data to a new CSV file
    df.to_csv('patient_0_test_7.csv', index=False)

    print("Data extracted and saved to 'patient_0_test_7.csv' successfully.")
# end of try statemement
except pd.errors.ParserError as e:
    print("Error reading the CSV file:", e)
# end of except statement


    # empty cells where there is no data
