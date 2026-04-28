```

import os

import pandas as pd




# Path to the folder containing XLSX files

folder_path = r'D:\New-query-14-day-and-older-published-cves\OUTPUT'




# Create a new folder named "OUTPUT" within the folder_path

output_folder_path = os.path.join(folder_path, 'OUTPUT')

os.makedirs(output_folder_path, exist_ok=True)




# Initialize an empty list to store dataframes

dfs = []




# Iterate over each file in the folder

for filename in os.listdir(folder_path):

    if filename.endswith('.xlsx'):

        file_path = os.path.join(folder_path, filename)

        # Read each XLSX file into a pandas dataframe

        df = pd.read_excel(file_path)

        # Extract file name without extension

        file_name_without_extension = os.path.splitext(filename)[0]

        # Add a new column with the file name (minus the extension)

        df['file_name'] = file_name_without_extension

        # Append the dataframe to the list

        dfs.append(df)




# Concatenate all dataframes into one

combined_df = pd.concat(dfs, ignore_index=True)




# Save the combined dataframe to a new XLSX file in the OUTPUT folder

output_file_path = os.path.join(output_folder_path, 'combined_data.xlsx')

combined_df.to_excel(output_file_path, index=False)




print("\nScript is done!")

```