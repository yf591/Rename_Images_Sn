# main.py

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from renamer import rename_images_sequentially
import shutil

def process_folder(original_folder_path, prefix):
    """
    Process the folder: copy, rename the folder, rename images, and remove unnecessary files.
    """
    if not original_folder_path:
        return

    try:
        # Get the original folder name
        folder_name = os.path.basename(original_folder_path)
        parent_dir = os.path.dirname(original_folder_path)

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

        # Copy the original folder to the new folder
        shutil.copytree(original_folder_path, new_folder_path)

        # Rename images sequentially in the new folder
        rename_images_sequentially(new_folder_path, new_folder_path, prefix)

        # Remove unnecessary files and folders in the new folder
        for item in os.listdir(new_folder_path):
            item_path = os.path.join(new_folder_path, item)
            if os.path.isfile(item_path):
                base, ext = os.path.splitext(item)
                try:
                    # Check if the file was renamed (has the format prefix_0001.ext)
                    int(base.split("_")[-1])
                except ValueError:
                    os.remove(item_path)
                    print(f"Removed file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed directory: {item_path}")

        messagebox.showinfo("Success", f"Processed and saved as {new_folder_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_folder():
    """
    Open a file dialog to select a folder and then process it.
    """
    folder_path = filedialog.askdirectory(
        title="Select Folder"
    )
    prefix = prefix_entry.get()
    if not prefix:
        prefix = "file"
    process_folder(folder_path, prefix)

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

    select_button = tk.Button(root, text="Select Folder", command=select_folder)
    select_button.pack(pady=20)

    root.mainloop()