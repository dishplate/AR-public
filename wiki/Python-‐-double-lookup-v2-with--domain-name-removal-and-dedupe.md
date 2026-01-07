~~~
#not working as intended for the depuing
#
import pandas as pd
import os

# Load the CSV file into a DataFrame
input_file = "your_file.csv"  # Replace with your input file path
df = pd.read_csv(input_file)

# Define column names
name_column1 = 'Column1'  # Replace with the actual name of column 1
name_column2 = 'Column2'  # Replace with the actual name of column 2

# Strip the domain part from hostnames directly in both columns
df[name_column1] = df[name_column1].apply(lambda x: x.split('.')[0] if pd.notna(x) else x)
df[name_column2] = df[name_column2].apply(lambda x: x.split('.')[0] if pd.notna(x) else x)

# Deduplicate entries within each column while retaining all rows
unique_col1 = df[name_column1].dropna().unique()
unique_col2 = df[name_column2].dropna().unique()

# Ensure all duplicates in Column2 are detected
df['Column2_in_Column1'] = df[name_column2].apply(lambda x: x if x in unique_col1 else 'Not Found')

# Ensure all duplicates in Column1 are detected
df['Column1_in_Column2'] = df[name_column1].apply(lambda x: x if x in unique_col2 else 'Not Found')

# Save the DataFrame to a new CSV file in the same folder
output_file = os.path.join(os.path.dirname(input_file), "output_file.csv")
df.to_csv(output_file, index=False)

~~~