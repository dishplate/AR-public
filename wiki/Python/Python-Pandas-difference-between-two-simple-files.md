~~~
#Works
#Need to fix this: The output file creates a new column 2 with a header and column 1 has no header. 
#run with manual python command line #python '.\Python\file.py'
import pandas as pd

# Define file paths
new_data_file = r'C:/Users/data.txt'
old_data_file = r'C:/Users/data1.txt'
output_file = r'C:/Users/processed.csv'

# Read the CSV files
new_data_df = pd.read_csv(new_data_file)
old_data_df = pd.read_csv(old_data_file)

# Extract relevant columns (Column 1 from new_data, Column 1 from old_data)
new_data_column = new_data_df.iloc[:, 0].astype(str).str.strip()
old_data_column = old_data_df.iloc[:, 0].astype(str).str.strip()

# Check if each value in Column 1 of old_data exists in Column 1 of new_data
old_data_df['ExistsInNewData'] = old_data_column.isin(new_data_column)

# Write the entire old_data_df with the new 'ExistsInNewData' column to a CSV file
old_data_df.to_csv(output_file, index=False)

print(f"Output written to {output_file}")
~~~