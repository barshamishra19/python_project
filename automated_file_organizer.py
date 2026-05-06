import os
import shutil

# Importing 'os' to work with directories and file paths
# Importing 'shutil' to perform file operations like moving files

# Set the folder you want to organize.
# Change this path if your target folder is in a different place.
target_directory = "./TestFolder"

# Map file extensions to the folder names you want to use.
# This dictionary acts as a rule book for sorting files
# You can add more extensions later if you want.
extension_map = {
    ".pdf": "Documents",   # All PDF files go to Documents folder
    ".docx": "Documents",  # Word files also go to Documents
    ".jpg": "Images",      # JPG images go to Images folder
    ".png": "Images",      # PNG images go to Images folder
    ".zip": "Archives"     # ZIP files go to Archives folder
}

# Check whether the target directory exists before continuing.
# Prevents errors if the folder path is wrong
if not os.path.exists(target_directory):
    print(f"Target directory not found: {target_directory}")
    print("Please update 'target_directory' to a valid folder path.")
else:
    # If folder exists, start organizing
    print(f"Organizing files in: {target_directory}")

    # Loop through every item (file/folder) in the target directory.
    for item_name in os.listdir(target_directory):

        # Create full path for each item (important for file operations)
        item_path = os.path.join(target_directory, item_name)

        # Only organize files (skip folders).
        # This ensures we don’t accidentally move directories
        if os.path.isfile(item_path):

            # Split file name and extension
            # Example: report.pdf -> ('report', '.pdf')
            _, extension = os.path.splitext(item_name)

            # Convert extension to lowercase for consistency
            # (handles cases like .JPG, .Pdf, etc.)
            extension = extension.lower()

            # Check if this extension is in our rule dictionary
            if extension in extension_map:

                # Get the folder name based on extension
                folder_name = extension_map[extension]

                # Create full path of the destination folder
                destination_folder = os.path.join(target_directory, folder_name)

                # Create the destination folder if it doesn't exist yet
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)  # Make new folder
                    print(f"Created folder: {folder_name}")

                # Create full path where file will be moved
                destination_path = os.path.join(destination_folder, item_name)

                # Inform user about the move action
                print(f"Moving {item_name} to {folder_name}")

                # Move the file into its destination folder
                shutil.move(item_path, destination_path)

            else:
                # If extension not in dictionary, skip the file
                print(f"Skipping {item_name} (no matching folder rule)")

    # Final message after all files are processed
    print("File organization complete.")
