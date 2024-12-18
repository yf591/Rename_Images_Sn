# renamer.py

import os
import shutil
from PIL import Image

def rename_images_sequentially(source_folder, destination_folder, prefix="file"):
    """
    Rename image files in the specified folder to sequential names with .jpg extension
    and copy them to the destination folder.
    Convert images with unsupported extensions to .jpg format.
    """
    supported_exts = {'.png', '.jpg', '.jpeg'}
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for i, file in enumerate(image_files, start=1):
        source_path = os.path.join(source_folder, file)
        base, ext = os.path.splitext(file)

        new_name = os.path.join(destination_folder, f"{prefix}_{i:04}.jpg")

        try:
            if ext.lower() in supported_exts:
                if ext.lower() != '.jpg':
                    im = Image.open(source_path)
                    rgb_im = im.convert('RGB')
                    rgb_im.save(new_name)
                    print(f"Converted '{file}' to '{os.path.basename(new_name)}'")
                else:
                    shutil.copy2(source_path, new_name)
                    print(f"Copied '{file}' to '{os.path.basename(new_name)}'")

            else:
                im = Image.open(source_path)
                rgb_im = im.convert('RGB')
                rgb_im.save(new_name)
                print(f"Converted '{file}' to '{os.path.basename(new_name)}'")
        except (IOError, OSError) as e:
            print(f"Could not process '{file}': {e}")

    print(f"Renaming and copying done: {os.listdir(destination_folder)}")