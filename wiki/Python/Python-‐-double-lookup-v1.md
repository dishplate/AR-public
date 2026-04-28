~~~
import pandas as pd
import os

# Load the CSV file into a DataFrame
input_file = '/home/ajay/Downloads/csv-data.csv'
df = pd.read_csv(input_file)
name_column1 = "Hostname"
name_column2 = "other hosts"

try:
# Check if column 2 values are in column 1 and create a third column with the match or 'Not Found'
    df['Is column 2 in col 1'] = df.apply(lambda row: row[name_column1] if row[name_column2] in df[name_column1].values else 'Not Found', axis=1)
    df['Is column 1 in col 2'] = df.apply(lambda row: row[name_column2] if row[name_column1] in df[name_column1].values else 'Not Found', axis=1)

# Save the DataFrame to a new CSV file in the same folder
    output_file = os.path.join(os.path.dirname(input_file), "output_file.csv")
    df.to_csv(output_file, index=False)
    print("Seems like it worked, file saved as" + " " + output_file)
except:
    print("something went wrong")

~~~