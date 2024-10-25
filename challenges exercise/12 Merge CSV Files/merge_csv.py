import csv

def merge_csv(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    # write data to output file based on field names
    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


# commands used in solution video for reference
if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')


import pandas as pd

# Read the two CSV files into DataFrames
df1 = pd.read_csv('class1.csv')
df2 = pd.read_csv('class2.csv')

# Get the list of columns in each DataFrame
columns_df1 = set(df1.columns)
columns_df2 = set(df2.columns)

# Find common columns
common_columns = columns_df1.intersection(columns_df2)

# Find unique columns in each DataFrame
unique_to_df1 = columns_df1 - columns_df2
unique_to_df2 = columns_df2 - columns_df1

# Display the results
print("Common columns:", common_columns)
print("Columns unique to class1.csv:", unique_to_df1)
print("Columns unique to class2.csv:", unique_to_df2)

# Merge the DataFrames on common columns using an outer join
merged_df = pd.merge(df1, df2, on=list(common_columns), how='outer')

# Function to format floats without decimals (keeping only integer part)
def format_float(value):
    if pd.isna(value):
        return value  # Leave NaN as is
    return "{:.0f}".format(value)  # Format float with no decimal part

# Apply the formatting to all numeric columns (integers and floats)
for col in merged_df.select_dtypes(include=['float', 'int']):
    merged_df[col] = merged_df[col].apply(format_float)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False, na_rep='')

print("Merged file saved as 'merged_file.csv'")
