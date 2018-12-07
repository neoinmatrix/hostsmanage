#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from Tkinter import *  # 导入 Tkinter 库


class HostFile:
    def __init__(self, file="/etc/hosts"):
        if os.path.exists(file) == False:
            raise ("not exist hosts file")
        self.file = file
        with open(file, "r") as f:
            info = f.read()
        info_arr_t = info.replace("\t", " ").split("\n")
        info_arr = []
        for v in info_arr_t:
            if v == "":
                continue
            info_arr.append(v)
        self.info = info_arr

    def write(self, info_arr=[]):
        if info_arr == []:
            info_arr = self.info
        info = "\n".join(info_arr)
        with open(file, "w") as f:
            f.write(info)


class WinForm:
    def __init__(self, info):
        root = Tk()  # 创建窗口对象的背景色
        root.title("hosts 管理工具")
        self.root = root
        lb = Listbox(root, width=60, height=50)  # 创建两个列表组件
        lb.pack()
        self.listbox = lb
        self.list_info = info
        self.bg_selected = "#f0f0ff"

    def render_listbox(self):
        for k, v in enumerate(self.list_info):
            self.listbox.insert(k, v)
            if "#" in list(v):
                self.listbox.itemconfig(k, bg="#f0f0ff")

    def click(self, *args):
        idx = int(self.listbox.curselection()[0])
        info = self.list_info[idx]
        if "#" in list(info):
            info.remove("#")
            self.listbox.itemconfig(idx, bg="#ffffff")

    def show(self):
        self.listbox.bind("<<ListboxSelect>>", self.click)
        self.root.mainloop()


if __name__ == "__main__":
    hf = HostFile()
    # print hf.info
    # print hf.file
    # hf.join()
    wf = WinForm(hf.info)
    wf.render_listbox()
    wf.show()
