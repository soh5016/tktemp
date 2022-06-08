from tkinter import *
from tkinter import messagebox, ttk
import sys
import webbrowser

class Gui(object):
    def __init__(self, root):
        root.title(self.__class__.__name__)
        root.geometry('300x50')
        
        root.option_add('*tearOff', False)
        self.menu = Menu()
        self.menudict = {}
        
        self.addMenu('file', 'ファイル(F)', 5)
        self.addMenuCommnad('file', '終了(X)', 3, self.menuFileExit)
        self.addMenu('help', 'ヘルプ(H)', 4)
        self.addMenuCommnad('help', 'バージョン情報(V)', 8, self.menuHelpVersion)

    def addMenu(self, keyname, label, underline):
        self.menudict[keyname] = Menu()
        self.menu.add_cascade(menu=self.menudict[keyname], label=label, underline=underline)
        root['menu'] = self.menu

    def addMenuCommnad(self, keyname, label, underline, function):
        self.menudict[keyname].add_command(label=label, underline=underline, command=function)
        root['menu'] = self.menu

        

    def menuFileExit(self):
        root.destroy()

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += ' Version 0.01(2022/06/08)\n'
        s += '©2022\n'
        s += 'with Python'
        messagebox.showinfo(self.__class__.__name__, s)


root = Tk()
Gui(root)
root.mainloop()
