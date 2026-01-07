~~~
import pandas as pd
import os

# Set the folder path containing the CSV files
folder_path = "your_folder_path_here"

# List all CSV files in the folder
files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Read and combine all CSV files
combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in files], ignore_index=True)

# Save the combined dataframe to a new CSV file in the same folder
output_path = os.path.join(folder_path, "combined_file.csv")
combined_df.to_csv(output_path, index=False)

print(f"Combined file saved to: {output_path}")
~~~