import re
import pandas as pd

# Path to the markdown file
file_path = './poster_table.md'

# Reading the contents of the markdown file
with open(file_path, 'r') as file:
    file_contents = file.read()

# Extracting table rows from the file contents
lines = file_contents.strip().split("\n")

# First two lines are headers, so we'll extract them separately
header = lines[0].strip().split("|")
rows = [line.strip().split("|")[1:-1] for line in lines[2:]]

# Creating a DataFrame from the rows
df = pd.DataFrame(rows, columns=[col.strip() for col in header[1:-1]])

# Function to split 'Group' and number
def split_group_name(group_name):
    word_part = group_name[:6]  # This will be 'Group'
    number_part = group_name[6:]  # This will be the number part
    #print(word_part, number_part)

    return int(number_part)

def new_group_name(group_name):
    word_part = group_name[:6]  # This will be 'Group'
    number_part = group_name[6:]  # This will be the number part
    #print(word_part, number_part)

    return word_part+" "+number_part

# Apply the function and create a 'Group Number' column
df['Group Number'] = df['Group Name'].apply(split_group_name)
df['Group Name'] = df['Group Name'].apply(new_group_name)

# Sorting by the 'Group Number' column
df_sorted = df.sort_values('Group Number').reset_index(drop=True)
print(df_sorted.head())

# Reconstructing the sorted markdown table
sorted_table = "| " + " | ".join(df_sorted.columns[:-1]) + " |\n"
sorted_table += "| " + " | ".join(["-" * len(col) for col in df_sorted.columns[:-1]]) + " |\n"

for _, row in df_sorted.iterrows():
    sorted_table += "| " + " | ".join(row[:-1]) + " |\n"

# Saving the sorted table back to a markdown file
output_path = './sorted_poster_table.md'
with open(output_path, 'w') as f:
    f.write(sorted_table)
