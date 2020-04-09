""""
Author: Thomas Hanna
FileWatcher.py:
    -The program watches your folder for any changes and updates the
    text file appropriately.
    -The directory we watch is file_path_watch, we read every file
    name in the directory and copy them into a .txt file in the
    location of your local Google Drive folder.
"""
import os
import time

# Google Drive Location:
file_path_drive = os.path.join("GoogleDrive/", 'ProgramList.txt')
# Watched Folder Location:
file_path_watch = "/Programs"

# Folder contents at start of program:
before = {(f, None) for f in os.listdir(file_path_watch)}


# Function for writing to Drive:
def update_drive(drive_path, watch_path):
    with open(drive_path, 'w') as f:
        for f_name in watch_path:
            f.write(os.path.splitext(f_name)[0] + "\n")


# Continues to watch:
while True:
    time.sleep(10)

    after = {(f, None) for f in os.listdir(file_path_watch)}
    added = [f for f in after if f not in before]
    removed = [f for f in before if f not in after]

    if len(added) > 0 or len(removed) > 0:
        print("file change")
        update_drive(file_path_drive, os.listdir(file_path_watch))

    before = after
