# zipper.py

import zipfile
import os

def zip_folder(folder_path, output_zip_path):
    """
    Compress the folder into a ZIP file.
    """
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Folder compressed into ZIP: {output_zip_path}")