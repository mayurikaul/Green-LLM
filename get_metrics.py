import pandas as pd

def extract_columns(input_file, output_file, columns):
    try:
        # Read the original Excel file
        df = pd.read_csv(input_file)

        # Check if columns exist in the DataFrame
        for col in columns:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' does not exist in the input file.")

        # Select the desired columns
        df_new = df[columns]

        # Write the selected columns to a new Excel file
        df_new.to_csv(output_file, index=False)
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define input and output files and the columns to extract
input_file = 'emissions.csv'
output_file = 'task_a_metrics.csv'
columns = ['run_id', 'emissions', 'cpu_power', 'ram_power', 'energy_consumed']

# Run the function
extract_columns(input_file, output_file, columns)
