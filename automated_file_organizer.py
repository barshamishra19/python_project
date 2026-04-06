import os
import shutil

# Set the folder you want to organize.
# Change this path if your target folder is in a different place.
target_directory = "./TestFolder"
# Map file extensions to the folder names you want to use.
# You can add more extensions later if you want.
extension_map = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".zip": "Archives"
}

# Check whether the target directory exists before continuing.
if not os.path.exists(target_directory):
    print(f"Target directory not found: {target_directory}")
    print("Please update 'target_directory' to a valid folder path.")
else:
    print(f"Organizing files in: {target_directory}")

    # Loop through every item in the target directory.
    for item_name in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item_name)

        # Only organize files (skip folders).
        if os.path.isfile(item_path):
            # Split file name and extension, e.g. report.pdf -> (report, .pdf)
            _, extension = os.path.splitext(item_name)
            extension = extension.lower()

            # Check if this extension is in our map.
            if extension in extension_map:
                folder_name = extension_map[extension]
                destination_folder = os.path.join(target_directory, folder_name)

                # Create the destination folder if it doesn't exist yet.
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    print(f"Created folder: {folder_name}")

                destination_path = os.path.join(destination_folder, item_name)
                print(f"Moving {item_name} to {folder_name}")

                # Move the file into its destination folder.
                shutil.move(item_path, destination_path)
            else:
                print(f"Skipping {item_name} (no matching folder rule)")

    print("File organization complete.")
