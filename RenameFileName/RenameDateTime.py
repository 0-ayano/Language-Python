from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
import tkinter.filedialog
import datetime
import re
import os

"""
関数名 : GetImageDate
引数　 : ファイル名(拡張子付き)
返り値 : 日時
説明　 : 写真の撮影日時または更新日時を取得する
"""
def GetImageDate(img_name):
    img = Image.open(img_name)
    # 拡張子がJPGの場合
    if img.format == "JPEG":
        exif = img.getexif()
        for id, value in exif.items():
            if TAGS.get(id, id) == "DateTime":
                ret = re.sub(" |:", "", value)
                return ret
            
    # 拡張子がPNGの場合
    elif img.format == "PNG":
        mtime = os.path.getmtime(img_name)
        ret = datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d%H%M%S")
        return ret
    
    # 拡張子がその他の場合
    else:
        return img_name
    

"""
関数名 : selectFile
引数　 : 
返り値 : 選択したファイル名
説明　 : ファイル選択ダイヤログを使って、ファイル名を取得する
"""
def selectFile():
    root = tk.Tk()
    root.withdraw()
    types = [ ("Image file", ".png .jpg .jpeg") ]
    target_files = tkinter.filedialog.askopenfilenames( filetypes = types, title = "open files" )
    return target_files

"""
関数名 : changeName
引数　 : 
返り値 : 
説明　 : 写真の名前を変更する
"""
def changeName():
        name = selectFile()
        for i, filepass in enumerate(name):
            # 変更後のファイル名の取得
            exts = [ext.replace("", "") for ext in filepass.split("/")]
            fe = [ext.replace(" ", "") for ext in exts[-1].split(".")]
            afterName = GetImageDate(filepass)
            
            # ファイル名の変更
            passname = exts[0]
            for count in exts[1:-1]:
                passname = f'{passname}/{count}'
            os.rename(filepass, f'{passname}/{afterName}.{fe[1]}')

# メイン処理
changeName()

"""
Reference
- [Python: ファイルの更新日時（タイムスタンプ）を取得する](https://step-learn.com/article/python/119-file-timestamp.html)
- [【Python】Pillowで画像のEXIF情報から日付を取得する](https://salapy.hatenablog.com/entry/2019/08/18/060635)
- [【 Python 】ファイル・フォルダをGUIで選択する方法まとめも](https://ito-room.com/python-filedialog/)
- [【仕事効率化】Pythonでファイル名を一括変更する方法](https://qiita.com/miyazakikna/items/b9c6d6d83ebcd529afd7)
- [【Python入門】ファイル名の一括変更プログラム](https://www.tomotaku.com/python-auto-rename/)
- [Pythonのfor文まとめ](https://qiita.com/ikuzak/items/0842c56131b6c3e333f2)
- [Pythonで写真の撮影日に合わせてファイル名を変更したい！](https://create-it-myself.com/know-how/howto-rename_photo_to_-taken_date/)
"""
