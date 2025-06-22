# Rename_Images_Sn

This is a GUI application that renames image files in a specified folder to sequential numbers.


## Features

*   Copies the specified folder and creates a new folder with `_Sn` appended to the end (e.g., `images` → `images_Sn`). (Updated 2024-12-23: Previously processed ZIP files.)
*   **Renames the images in the new folder (`_Sn` folder) with a specified prefix (or the default `file`) and sequential numbers (e.g., `file_0001.jpg`, `image_0002.png`).** (Updated 2024-12-23: Previously zipped the `_Sn` folder.)
*   Maintains the original extension for `.png`, `.jpg`, and `.jpeg` images. Other image formats are converted to `.jpg` format. (Updated 2024-12-18: Previously converted all to `.jpg`. Updated 2024-12-23: Now maintains extensions for `.png`, `.jpg`, and `.jpeg`.)
*   **After processing, only the sequentially numbered image files will remain in the `_Sn` folder. Other files and folders will be deleted.** (Updated 2024-12-23: Added functionality to remove unnecessary files and folders)
*   Easy to use with a Tkinter-based GUI.
*   The filename prefix can be freely entered and changed on the GUI. If left blank, the default `file` will be used.


## Operating Environment

*   Python 3.x
*   Required packages are listed in `requirements.txt`.


## Installation

```bash
git clone https://github.com/yf591/Rename_Images_Sn.git
cd Rename_Images_Sn

# Create virtual environment
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Install required packages
pip install -r requirements.txt
```


## Usage

1. Run `main.py`.

    ```bash
    python main.py
    ```

2. In the displayed GUI, enter an optional prefix in the input field under "Enter prefix for filenames (optional):" (e.g., entering "image" will result in "image_0001.jpg", "image_0002.jpg", ...). Leaving it blank will result in "file_0001.jpg", ...
3. Click the "Select Folder" button. (Updated 2024-12-23: Previously "Select ZIP File" button.)
4. In the file selection dialog, select the folder you want to process.
5. The selected folder will be copied, image files will be renamed, and a new folder with `_Sn` appended to the end will be created. **Only the sequentially numbered image files will remain in the new folder.**


## Repository Structure

```
Rename_Images_Sn/
├── README.md           # English README (this file)
├── README-ja.md        # Japanese README
├── main.py             # Main program (GUI) (Updated 2024-12-23: Modified to process folders. Added functionality to remove unnecessary files and folders)
├── renamer.py          # Image renaming function (Updated 2024-12-23: Modified to maintain extensions for .png, .jpg, .jpeg)
└── requirements.txt    # Required packages
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
* 2024-12-23:
    *   Updated `main.py` to process folders instead of ZIP files. Removed ZIP file processing.
    *   Updated `main.py` to add functionality to remove files and folders other than sequentially numbered files in the `_Sn` folder.
    *   Updated `renamer.py` to maintain extensions for `.png`, `.jpg`, and `.jpeg`.
    *   Deleted `zipper.py`.
    *   Updated `README.md` and `README-ja.md` to reflect the changes.