import os

# 現在開いているファイルのディレクトリの位置を取得
TOP_DIR = os.path.dirname(__file__)
print(TOP_DIR)
# imageディレクトリを指定
IMG_DIR = os.path.join(TOP_DIR, "image")
print(IMG_DIR)