# Automated File Organizer

## Description

Automated File Organizer is a simple Python script that sorts files in a folder into organized subfolders based on their file extensions. It's designed to help you quickly clean up cluttered directories by grouping similar files together.

## How It Works

The script:
1. Scans a target directory for all files
2. Identifies each file's extension (e.g., .pdf, .jpg, .zip)
3. Maps the extension to a category folder (Documents, Images, Archives, etc.)
4. Creates the category folder if it doesn't exist
5. Moves the file into its matching folder
6. Prints progress messages so you can see what's happening

Files without a matching rule are skipped and left in place.

## Getting Started

### Setting the Target Directory

Open `automated_file_organizer.py` and find this line at the top:

```python
target_directory = "./TestFolder"
```

Replace `"Test"` with your actual folder name or path. Examples:

```python
# Organize a folder called "Downloads"
target_directory = os.path.join(os.path.expanduser("~"), "Downloads")

# Or use an absolute path
target_directory = r"C:\Users\YourName\Desktop\MyFiles"
```

### Customizing File Extensions

Edit the `extension_map` dictionary to add or change categories:

```python
extension_map = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".zip": "Archives"
}
```

Add new extensions as needed (e.g., `".txt": "Documents"`).

### How to Run

1. Open a command prompt or PowerShell
2. Navigate to the script's folder
3. Run the script:

```bash
python automated_file_organizer.py
```

The script will organize your files and display progress messages as it works.

## Requirements

- Python 3.x
- No external packages needed (uses only os and shutil)

## Example Output

```
Organizing files in: C:\Users\YourName\Desktop\Test
Created folder: Documents
Moving report.pdf to Documents
Moving notes.docx to Documents
Moving photo.jpg to Images
Created folder: Archives
Moving backup.zip to Archives
Skipping readme.txt (no matching folder rule)
File organization complete.
```

## Notes

- The script only moves files, not existing folders in the target directory
- Files with unmatched extensions are skipped (not deleted)
- Use this script on test folders first if you're unsure about the results
