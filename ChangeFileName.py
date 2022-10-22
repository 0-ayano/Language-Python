import os
import re
import glob
import tkinter as tk
import tkinter.filedialog

class changeFileName():  
    def selectFile( self ):
        root = tk.Tk()
        root.withdraw()
        types = [ ("all file", "*.*"), ("画像ファイル(JPG)", "*.jpg"), ("画像ファイル（PNG）", "*.png") ]
        target_files = tkinter.filedialog.askopenfilenames( filetypes = types, title = "open files" )
        return target_files

    def selectFolder( self ):
        root = tk.Tk()
        root.withdraw()
        target_dir = tkinter.filedialog.askdirectory(mustexist=True)
        target_files = glob.glob(os.path.join(target_dir, "*"))
        return target_files

    def showFiles(  self , *name ):
        for filepass in name:
            print( filepass )

    def changeName_1( self ):
        name = self.selectFile()
        AfterName = input(">>")
        i,passname = 1, ""
        for filepass in name:
            i_0 = str(i).zfill(3)
        for filepass in name:
            i_0 = str(i).zfill(3)
            exts = [ext.replace(" ", "") for ext in filepass.split("/")]
            fe = [ext.replace(" ", "") for ext in exts[-1].split(".")]
            passname = exts[0]
            for count in exts[1:-1]:
                passname = f'{passname}/{count}'
            os.rename(name[i-1], f'{passname}/{AfterName}_{i_0}.{fe[1]}')
            i = i + 1

    def changeName_2( self ):
        name = self.selectFolder()
        AfterName = input(">>")
        i = 1
        for filepass in name:
            i_0 = str(i).zfill(3)
            exts = [ext.replace(" ", "") for ext in filepass.split("\\")]
            fe = [ext.replace(" ", "") for ext in exts[1].split(".")]
            os.rename(name[i-1], f'{exts[0]}\{AfterName}_{i_0}.{fe[1]}')
            i = i + 1


test = changeFileName()
test.changeName_1()

"""
参考サイト
[【 Python 】ファイル・フォルダをGUIで選択する方法まとめも](https://ito-room.com/python-filedialog/)
[【仕事効率化】Pythonでファイル名を一括変更する方法](https://qiita.com/miyazakikna/items/b9c6d6d83ebcd529afd7)
[【Python入門】ファイル名の一括変更プログラム](https://www.tomotaku.com/python-auto-rename/)
"""