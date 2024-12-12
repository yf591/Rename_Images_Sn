# Rename_Images_Sn

A GUI application to rename images in a specified ZIP file with sequential numbers.


## Features

*   Extracts images from a ZIP file and renames them with a specified prefix (or the default `file`) and sequential numbers (e.g., `file_0001.jpg`, `image_0002.png`).
*   Does not modify the original folder. Instead, creates a new folder named `original_folder_name_Sn` and stores the renamed images there.
*   Compresses the `original_folder_name_Sn` folder containing the renamed images into a new ZIP file (`original_folder_name_Sn.zip`).
*   Provides an easy-to-use GUI with Tkinter.
*   Allows you to freely enter a prefix for filenames in the GUI. If left blank, the default `file` prefix is used.


## Requirements

*   Python 3.x
*   Required packages are listed in `requirements.txt`. **(Currently, `requirements.txt` is empty. This application uses only the Python standard library.)**


## Installation

```bash
git clone https://github.com/your_username/Rename_Images_Sn.git
cd Rename_Images_Sn
pip install -r requirements.txt
```


## Usage

1. Run `main.py`.

    ```bash
    python main.py
    ```

2. In the GUI, enter an optional prefix in the input field under "Enter prefix for filenames (optional):" (e.g., entering "image" will result in "image_0001.jpg", "image_0002.jpg", ...). If left blank, it will be "file_0001.jpg", ...
3. Click the "Select ZIP File" button.
4. In the file selection dialog, select the ZIP file you want to process.
5. The selected ZIP file will be extracted, the image files will be renamed, and saved as a new ZIP file. The original folder will remain unchanged.


## Repository Structure

```
Rename_Images_Sn/
├── README.md           # English README (this file)
├── README-ja.md        # Japanese README
├── main.py             # Main program (GUI)
├── renamer.py          # Image renaming function
├── zipper.py           # ZIP compression/decompression function
└── requirements.txt    # Required packages
```


## Disclaimer

The developer is not responsible for any damages, losses, or disadvantages arising from the use of this application. Use at your own risk. This application is provided "as is" without any warranty of any kind.


## License

MIT License


## Developer

yf591