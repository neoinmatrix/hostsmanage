#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *  # 导入 Tkinter 库

root = Tk()  # 创建窗口对象的背景色

root.title("hosts 管理工具")

# 进入消息循环
file = "/etc/hosts"

with open(file, "r") as f:
    info = f.read()
info_arr_t = info.replace("\t", " ").split("\n")
info_arr = []
for v in info_arr_t:
    if v == "":
        continue
    info_arr.append(v)

listb = Listbox(root, width=60, height=50)  # 创建两个列表组件
listb.pack()


def render(listbox, info):
    for k, v in enumerate(info):
        listbox.insert(k, v)
        if "#" in list(v):
            listbox.itemconfig(k, bg="#f0f0ff")


def show_msg(*args):
    print listb.curselection()

    # render(listb,info)



listb.bind("<<ListboxSelect>>",show_msg)

render(listb, info_arr)
root.mainloop()
