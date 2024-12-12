# renamer.py

import os
import shutil

def rename_images_sequentially(source_folder, destination_folder, prefix="file"):
    """
    Rename image files (.png, .jpg, .jpeg) in the specified folder to sequential names
    and copy them to the destination folder.
    """
    supported_exts = {'.png', '.jpg', '.jpeg'}
    images = sorted([f for f in os.listdir(source_folder) if os.path.splitext(f)[1].lower() in supported_exts])

    for i, file in enumerate(images, start=1):
        ext = os.path.splitext(file)[1]
        new_name = os.path.join(destination_folder, f"{prefix}_{i:04}{ext}")
        source_path = os.path.join(source_folder, file)

        # Copy the renamed file to the destination folder
        shutil.copy2(source_path, new_name)

    print(f"Renaming and copying done: {os.listdir(destination_folder)}")