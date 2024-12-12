# Rename_Images_Sn

指定されたZIPファイル内の画像を連番にリネーム（rename）するGUIアプリケーションです。


## 機能

*   ZIPファイル内の画像を抽出し、指定されたプレフィックス（またはデフォルトの `file`）と連番でリネームします（例：`file_0001.jpg`、`image_0002.png`）。
*   元のフォルダは変更せず、`元のフォルダ名_Sn` という新しいフォルダを作成して、リネームした画像を格納します。
*   リネームされた画像を格納した `元のフォルダ名_Sn` フォルダをZIP圧縮して、新しいZIPファイル（`元のフォルダ名_Sn.zip`）を作成します。
*   Tkinterを使用したGUIで、簡単に操作できます。
*   ファイル名のプレフィックスは、GUI上で自由に入力して変更できます。空欄の場合は、デフォルトの `file` が使用されます。


## 動作環境

*   Python 3.x
*   必要なパッケージは `requirements.txt` に記載されています。**（現在、`requirements.txt` は空欄です。このアプリケーションは Python の標準ライブラリのみを使用しています。）**


## インストール方法

```bash
git clone https://github.com/yf591/Rename_Images_Sn.git
cd Rename_Images_Sn
pip install -r requirements.txt
```


## 使用方法

1. `main.py` を実行します。

    ```bash
    python main.py
    ```

2. 表示されたGUIで「Enter prefix for filenames (optional):」の下の入力欄に、任意のプレフィックスを入力します（例：「image」と入力すると、「image_0001.jpg」、「image_0002.jpg」、... となります）。空欄のままにすると、「file_0001.jpg」、...となります。
3. 「Select ZIP File」ボタンをクリックします。
4. ファイル選択ダイアログで、処理したいZIPファイルを選択します。
5. 選択したZIPファイルが解凍され、画像ファイルがリネームされて、新しいZIPファイルとして保存されます。元のフォルダは変更されません。


## リポジトリ構成

```
Rename_Images_Sn/
├── README.md           # 英語版README
├── README-ja.md        # 日本語版README（このファイル）
├── main.py             # メインプログラム（GUI）
├── renamer.py          # 画像リネーム機能
├── zipper.py           # ZIP圧縮・解凍機能
└── requirements.txt    # 必要なパッケージ
```


## 免責事項

このアプリケーションの使用によって生じたいかなる損害、損失、不利益などについて、開発者は一切の責任を負いません。自己責任でご使用ください。このアプリケーションは現状のまま提供され、いかなる保証もありません。


## ライセンス

MIT License


## 開発者

yf591