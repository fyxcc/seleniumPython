import win32api, win32con
import time
from tkinter import Tk


class ActionExe():
    def __init__(self):
        self.r = Tk()

    # 将内容复制到剪切板
    def add_to_clipboard(self, string):
        self.r.withdraw()
        self.r.clipboard_clear()
        self.r.clipboard_append(string)
        self.r.update()
        self.r.destroy()


    # 获取剪切板的内容
    def get_clipboard(self):
        r=Tk()
        clipboard_text = r.clipboard_get()
        return clipboard_text

    # 按下ctrl+v
    def paste_method(self):
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)

