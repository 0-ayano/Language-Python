import webbrowser
import csv
import tkinter as tk
import tkinter.filedialog

def selectFile():
        root = tk.Tk()
        root.withdraw()
        types = [ ("all file", "*.*" )]
        target_files = tkinter.filedialog.askopenfilenames( filetypes = types, title = "open files" )
        return target_files

webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"))
name = selectFile()[0].split("/")[-1]

with open(name, 'r', encoding="utf-8") as f:
    csv.reader(f)
    for url in csv.reader(f):
        print("%s" %all)
        webbrowser.get('brave').open(url[0])


