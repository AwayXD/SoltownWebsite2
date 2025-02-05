import os

def rename_jpeg_files(folder_path):
    # Get all files in the folder that end with .jpeg
    jpeg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpeg')]
    
    # Sort the files for consistent numbering
    jpeg_files.sort()
    
    # Rename each file to a sequential number
    for index, filename in enumerate(jpeg_files, start=1):
        # Construct the full old and new file paths
        old_path = os.path.join(folder_path, filename)
        new_name = f"{index}.jpeg"
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# Example usage:
# Specify the folder path containing the .jpeg files
folder_path = "C:\\Users\\Speak\\Desktop\\Coding Projects\\SoltownWebsite\\images\\media"
rename_jpeg_files(folder_path)
