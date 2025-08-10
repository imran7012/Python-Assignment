import os
import sys
import shutil
from datetime import datetime

def backup_files(source, destination):
    # It will Check for source and destination folders exist
    if not os.path.exists(source):
        print(" Source folder not found!")
        return
    if not os.path.exists(destination):
        print(" Destination folder not found!")
        return

    # Go through each file in the source folder
    for file in os.listdir(source):
        source_path = os.path.join(source, file)

        # Only copy files (not folders)
        if os.path.isfile(source_path):
            dest_path = os.path.join(destination, file)

            # If file exists in destination, add a timestamp
            if os.path.exists(dest_path):
                time_now = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(file)
                file = f"{name}_{time_now}{ext}"
                dest_path = os.path.join(destination, file)

            # Copy the file
            shutil.copy2(source_path, dest_path)
            print(f" Copied: {file}")

if len(sys.argv) != 3:
    print("Usage: python backup.py <source_folder> <destination_folder>")
else:
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    backup_files(source_folder, destination_folder)
