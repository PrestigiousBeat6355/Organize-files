import os
import shutil
import datetime

# Prompt the user to enter the source folder
source_folder = input("Enter the source folder path: ")

# Prompt the user to enter the destination folder
destination_folder = input("Enter the destination folder path: ")

# Get a list of all files in the source folder and its subfolders
file_list = []
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_list.append(os.path.join(root, file))

# Organize files by their modified date and file types
for file_path in file_list:
    # Get the modified date of the file
    modified_time = os.path.getmtime(file_path)
    modified_date = datetime.datetime.fromtimestamp(modified_time)

    # Create the destination folder based on the modified date (YYYY_MM format)
    folder_name = modified_date.strftime("%Y_%m")
    destination_path = os.path.join(destination_folder, folder_name)

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_path, exist_ok=True)

    # Get the file extension and name
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    file_name = os.path.basename(file_path)

    # Handle specific conditions for file names
    # Create a separate folder for the file type or place it in the "General" folder
    if file_extension:
        type_folder = file_extension[1:].upper()
    else:
        type_folder = "General"
    type_folder_path = os.path.join(destination_path, type_folder)
    os.makedirs(type_folder_path, exist_ok=True)
    shutil.copy2(file_path, type_folder_path)

print("File organization completed!")
input("Press Enter to close the window")
