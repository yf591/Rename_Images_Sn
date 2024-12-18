# Rename_Images_Sn

This is a GUI application that renames image files in a specified ZIP file to sequential numbers.


## Features

*   Extracts images from a ZIP file and renames them with a specified prefix (or the default `file`) and sequential numbers (e.g., `file_0001.jpg`, `image_0002.png`).
*   **Converts all supported image formats to `.jpg` format before sequential numbering.** (Updated 2024-12-18: Previously only supported `jpg`, `jpeg`, and `png`.)
*   Creates a new folder named `original_folder_name_Sn` without modifying the original folder and stores the renamed images in it.
*   Compresses the `original_folder_name_Sn` folder containing the renamed images into a new ZIP file (`original_folder_name_Sn.zip`).
*   Easy to use with a Tkinter-based GUI.
*   The filename prefix can be freely entered and changed on the GUI. If left blank, the default `file` will be used.


## Operating Environment

*   Python 3.x
*   Required packages are listed in `requirements.txt`.


## Installation

```bash
git clone https://github.com/yf591/Rename_Images_Sn.git
cd Rename_Images_Sn
pip install -r requirements.txt
```


## Usage

1. Run `main.py`.

    ```bash
    python main.py
    ```

2. In the displayed GUI, enter an optional prefix in the input field under "Enter prefix for filenames (optional):" (e.g., entering "image" will result in "image_0001.jpg", "image_0002.jpg", ...). Leaving it blank will result in "file_0001.jpg", ...
3. Click the "Select ZIP File" button.
4. In the file selection dialog, select the ZIP file you want to process.
5. The selected ZIP file will be extracted, image files will be renamed, and saved as a new ZIP file. The original folder will not be changed.


## Repository Structure

```
Rename_Images_Sn/
├── README.md           # English README (this file)
├── README-ja.md        # Japanese README
├── main.py             # Main program (GUI)
├── renamer.py          # Image renaming function (Updated 2024-12-18: Added image conversion functionality)
├── zipper.py           # ZIP compression/decompression function
└── requirements.txt    # Required packages (Updated 2024-12-18: Added Pillow)
```


## Disclaimer

The developer is not responsible for any damages, losses, or disadvantages caused by the use of this application. Use at your own risk. This application is provided as is, with no warranties.


## License

MIT License


## Developer

yf591


## Update History

* 2024-12-18:
    *   Updated `renamer.py` to add the functionality of converting image files other than `jpg`, `jpeg`, and `png` to `.jpg` and numbering them sequentially.
    *   Updated `requirements.txt` to add the `Pillow` library required for image conversion.
    *   Deleted `import shutil` in `main.py`
    *   Added annotations for changes and dates to `README.md` and `README-ja.md`.