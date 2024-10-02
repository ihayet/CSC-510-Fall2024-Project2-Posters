# Function to generate a 3-column markdown table for group directories and their posters
import os
base_path = "C:/Users/Andre/Documents/NCSU/SE24FALLTA/posters"


def generate_poster_table(folder_structure):
    poster_table = "| Group Name | Poster 1 | Poster 2 |\n|------------|----------|----------|\n"
    
    # Traverse through the folder structure to find the posters
    for path in folder_structure:
        group_name = os.path.basename(path)
        # Identify group directories
        if os.path.isdir(os.path.join(base_path, path)):
            poster1 = ""
            poster2 = ""
            # Check files inside the group folder
            for file_name in os.listdir(os.path.join(base_path, path)):
                if "Poster1" in file_name:
                    poster1 = f"[Poster1](./{os.path.join(path, file_name)})"
                elif "Poster2" in file_name:
                    poster2 = f"[Poster2](./{os.path.join(path, file_name)})"
            
            # Append the row for this group with links
            poster_table += f"| {group_name} | {poster1} | {poster2} |\n"
    
    return poster_table

# Generate the poster table
folders = os.listdir(".")
#remove anything that is not a directory

for folder in folders:
    if not os.path.isdir(folder):
        folders.remove(folder)

poster_markdown_table = generate_poster_table(folders)
with open("poster_table.md", "w") as file:
    file.write(poster_markdown_table)