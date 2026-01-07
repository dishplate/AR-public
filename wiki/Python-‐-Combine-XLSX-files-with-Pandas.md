~~~
#This works 11/21/2024
#This script just combines multiple xlxs files in the same folder. The output file is created in the same folder.
import pandas as pd
import os

# Set the folder path containing the xlsx files
folder_path = '/home/ajay/Downloads/'

# List all xlsx files in the folder
files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]

# Read and combine all files
combined_df = pd.concat([pd.read_excel(os.path.join(folder_path, file)) for file in files], ignore_index=True)

# Save the combined dataframe to a new xlsx file in the same folder
output_path = os.path.join(folder_path, "combined_file.xlsx")
combined_df.to_excel(output_path, index=False)

print(f"Combined file saved to: {output_path}")


~~~