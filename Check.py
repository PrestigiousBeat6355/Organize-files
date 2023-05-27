import os

def calculate_missing_files_percentage(folder1, folder2):
    total_files = 0
    missing_files = 0
    encountered_files = set()

    # Count total files in folder1
    for root, dirs, files in os.walk(folder1):
        for file in files:
            if not file.startswith("WA"):  # Exclude files starting with "WA"
                total_files += 1
                encountered_files.add(file)

    # Compare files in folder2 with folder1
    for root, dirs, files in os.walk(folder2):
        for file in files:
            if not file.startswith("WA"):  # Exclude files starting with "WA"
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder2)
                corresponding_path = os.path.join(folder1, relative_path)

                if not os.path.exists(corresponding_path) and file not in encountered_files:
                    missing_files += 1

    if total_files == 0:
        missing_percentage = 0
    else:
        missing_percentage = (missing_files / total_files) * 100

    return missing_percentage

# Prompt the user to enter the folder paths
folder1 = input("Enter the source folder path: ")
folder2 = input("Enter the destination folder path: ")

missing_percentage = calculate_missing_files_percentage(folder1, folder2)
print(f"Percentage of missing files in {folder2} or its subfolders: {missing_percentage:.2f}%")
input("Press Enter to close the window")
