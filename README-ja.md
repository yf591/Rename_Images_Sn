# Rename_Images_Sn

指定されたフォルダ内の画像ファイルを連番にリネーム（rename）するGUIアプリケーションです。


## 機能

*   指定されたフォルダをコピーし、末尾に `_Sn` を付けた新しいフォルダを作成します (例: `images` → `images_Sn`)。(2024-12-23 更新: 以前はZIPファイルを処理していました。)
*   **新しいフォルダ (`_Sn` フォルダ) 内の画像ファイルを、指定されたプレフィックス（またはデフォルトの `file`）と連番でリネームします（例：`file_0001.jpg`、`image_0002.png`）。**(2024-12-23 更新: 以前は `_Sn` フォルダをZIP化していました。)
*   `.png`, `.jpg`, `.jpeg` の画像は元の拡張子を維持します。それ以外の画像形式は、`.jpg` 形式に変換します。(2024-12-18 更新: 以前はすべてを `.jpg` に変換していました。2024-12-23 更新: `.png`, `.jpg`, `.jpeg` は拡張子を維持するようになりました。)
*   **処理後、`_Sn` フォルダ内には連番化された画像ファイルのみが残ります。その他のファイルやフォルダは削除されます。**(2024-12-23 更新: 不要ファイル・フォルダ削除機能の追加)
*   Tkinterを使用したGUIで、簡単に操作できます。
*   ファイル名のプレフィックスは、GUI上で自由に入力して変更できます。空欄の場合は、デフォルトの `file` が使用されます。


## 動作環境

*   Python 3.x
*   必要なパッケージは `requirements.txt` に記載されています。


## インストール方法

```bash
git clone https://github.com/yf591/Rename_Images_Sn.git
cd Rename_Images_Sn

# 仮想環境を作成
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# 必要なパッケージをインストール
pip install -r requirements.txt
```


## 使用方法

1. `main.py` を実行します。

    ```bash
    python main.py
    ```

2. 表示されたGUIで「Enter prefix for filenames (optional):」の下の入力欄に、任意のプレフィックスを入力します（例：「image」と入力すると、「image_0001.jpg」、「image_0002.jpg」、... となります）。空欄のままにすると、「file_0001.jpg」、...となります。
3. 「Select Folder」ボタンをクリックします (2024-12-23 更新: 以前は「Select ZIP File」ボタンでした)。
4. ファイル選択ダイアログで、処理したいフォルダを選択します。
5. 選択したフォルダがコピーされ、画像ファイルがリネームされて、末尾に `_Sn` が付いた新しいフォルダが作成されます。**新しいフォルダには、連番化された画像ファイルのみが残ります。**


## リポジトリ構成

```
Rename_Images_Sn/
├── README.md           # 英語版README
├── README-ja.md        # 日本語版README（このファイル）
├── main.py             # メインプログラム（GUI）(2024-12-23 更新: フォルダを処理するように変更。不要ファイル・フォルダ削除機能の追加)
├── renamer.py          # 画像リネーム機能 (2024-12-23 更新: .png, .jpg, .jpeg の拡張子を維持するように変更)
└── requirements.txt    # 必要なパッケージ
```


## 免責事項

このアプリケーションの使用によって生じたいかなる損害、損失、不利益などについて、開発者は一切の責任を負いません。自己責任でご使用ください。このアプリケーションは現状のまま提供され、いかなる保証もありません。


## ライセンス

MIT License


## 開発者

yf591


## 更新履歴

* 2024-12-18:
    *   `renamer.py` を更新し、`jpg`, `jpeg`, `png` 以外の画像ファイルも `.jpg` に変換して連番化する機能を追加。
    *   `requirements.txt` を更新し、画像変換に必要な `Pillow` ライブラリを追加。
    *   `main.py`を更新し、`import shutil`を削除。
    *   `README.md` と `README-ja.md` に変更内容と変更日の注釈を追加。
* 2024-12-23:
    *   `main.py` を更新し、フォルダを処理するように変更。ZIPファイルの処理を削除。
    *   `main.py` を更新し、`_Sn` フォルダ内に連番化したファイル以外のファイルやフォルダが存在する場合、それらを削除する機能を追加。
    *   `renamer.py` を更新し、`.png`, `.jpg`, `.jpeg` の拡張子を維持するように変更。
    *   `zipper.py` を削除。
    *   `README.md` と `README-ja.md` を更新し、変更内容を反映。

