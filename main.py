# main.py

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import zipfile
from renamer import rename_images_sequentially
from zipper import zip_folder
# import shutil # 削除

def process_zip_file(zip_path, prefix):
    """
    Unzip the ZIP file, rename images, and re-zip the folder.
    """
    if not zip_path:
        return

    try:
        # Extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            extract_folder = os.path.splitext(zip_path)[0]
            zipf.extractall(extract_folder)

        # Get the original folder name
        folder_name = os.path.basename(extract_folder)
        parent_dir = os.path.dirname(extract_folder)

        # Create a new folder name (a folder with _Sn appended)
        new_folder_name = folder_name + "_Sn"
        new_folder_path = os.path.join(parent_dir, new_folder_name)

        # Process to avoid duplication of existing folder names
        if os.path.exists(new_folder_path):
            count = 1
            while True:
                new_folder_name = f"{folder_name}_Sn_{count}"
                new_folder_path = os.path.join(parent_dir, new_folder_name)
                if not os.path.exists(new_folder_path):
                    break
                count += 1

        # Create a new folder
        os.makedirs(new_folder_path)

        # Rename images sequentially and copy to new folder
        rename_images_sequentially(extract_folder, new_folder_path, prefix)

        # Compress the renamed folder into a ZIP file
        new_zip_path = os.path.join(parent_dir, f"{new_folder_name}.zip")
        zip_folder(new_folder_path, new_zip_path)

        messagebox.showinfo("Success", f"Processed and saved as {new_zip_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_zip_file():
    """
    Open a file dialog to select a ZIP file and then process it.
    """
    file_path = filedialog.askopenfilename(
        title="Select ZIP file",
        filetypes=(("ZIP files", "*.zip"), ("all files", "*.*"))
    )
    prefix = prefix_entry.get()
    if not prefix:
        prefix = "file"
    process_zip_file(file_path, prefix)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rename_Images_Sn")

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate window size (approximately 1/4 of the screen)
    window_width = screen_width // 2
    window_height = screen_height // 2

    # Set window size and position
    root.geometry(f"{window_width}x{window_height}+{window_width//2}+{window_height//2}")

    # Prefix input
    prefix_label = tk.Label(root, text="Enter prefix for filenames (optional):")
    prefix_label.pack(pady=(10,0))
    prefix_entry = tk.Entry(root)
    prefix_entry.pack(pady=(0,10))

    select_button = tk.Button(root, text="Select ZIP File", command=select_zip_file)
    select_button.pack(pady=20)

    root.mainloop()