```

import pandas as pd

import os

from datetime import datetime




# Get the current date

current_date = datetime.now().strftime('%Y-%m-%d')




# Path to the folder containing CSV files, this will process all files in the folder that is csv

folder_path = r'D:\new folder'




# Create a new folder named "OUTPUT" within the folder_path

output_folder_path = os.path.join(folder_path, 'OUTPUT')

os.makedirs(output_folder_path, exist_ok=True)




# Grab csv files in the folder_path

csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Loop through each file in the directory

for file in csv_files:

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)




    # Count the number of cells in 'cntCritical' that are greater than zero

    count_greater_than_zero = (df['cntCritical'] > 0).sum()

    print(f"Number of 'cntCritical' cells greater than zero in {file}: {count_greater_than_zero}")




    # Convert the 'hostName' column to lowercase

    df['hostName'] = df['hostName'].str.lower()




    # Split the 'hostName' column based on periods and create new columns dynamically

    max_splits = df['hostName'].str.count('.').max()

    split_columns = [f'hostName Split_{i+1}' for i in range(max_splits)]




    # Split the 'hostName' column and keep all split parts

    split_data = df['hostName'].str.split('.', expand=True)

    split_data.columns = split_columns[:len(split_data.columns)]




    # Combine the split columns with the original DataFrame

    df = pd.concat([df, split_data], axis=1)




    # Deduplicate based on the first split column (Should be 'hostName Split_1)

    df = df.drop_duplicates(subset=split_columns[0])




    # Prevent the removal of rows that have a blank 'agentKey' cell

    df_rem_agent = df[(~df['agentKey'].duplicated()) | df['agentKey'].isna()]




    # Rearrange columns in the desired order, cntFindings is the total vulnerabilities, obeying the vuln filter in the query builder

    column_order = ['hostName Split_1', 'hostName', 'cntCritical', 'cntSevere', 'cntModerate', 'exploitCount', 'malwareCount', 'osDescription', 'ip', 'osCertainty', 'lastScanTimeIso']




    # Create a new DataFrame with the specified column order and all other columns

    new_df = df_rem_agent[column_order + [col for col in df_rem_agent.columns if col not in column_order]]




    # Sort the DataFrame by the 'Critical vulns' column in descending order

    df = new_df.sort_values(by='cntCritical', ascending=False)




    # Assuming df is your DataFrame containing all columns

    columns_to_keep = ['hostName', 'cntCritical', 'cntSevere',

                       'cntModerate', 'exploitCount', 'malwareCount',

                       'osDescription', 'ip',

                       'lastScanTimeIso']




    # Drop columns that are not in the list

    df = df.drop(columns=df.columns.difference(columns_to_keep))




    # Construct the output file path with xlsx extension

    output_file_name = os.path.splitext(file)[0] + '_' + current_date + '.xlsx'

    xlsx_file_path = os.path.join(output_folder_path, output_file_name)




    # Write the DataFrame to an Excel file

    writer = pd.ExcelWriter(xlsx_file_path, engine='xlsxwriter')

    df.to_excel(writer, index=False)




    # Get the xlsxwriter workbook and worksheet objects

    workbook = writer.book

    worksheet = writer.sheets['Sheet1']  # Assuming the sheet name is 'Sheet1'




    # Define the format for bold and red font

    bold_red_format = workbook.add_format({'bold': True, 'font_color': 'red'})




#   # Apply the format to the rows that meet the condition

#     for row_num, crit_vuln in enumerate(df['cntCritical'], start=2):

#         if 2 <= row_num <= 11 and crit_vuln >= 1:

#             worksheet.set_row(row_num - 1, None, bold_red_format)




    writer._save()

    print(f"Processed data written to: {xlsx_file_path}")




print("\nSCRIPT COMPLETE")
```