# @Time : 2022/8/14 10:58
# @Author : 龙锐 942121483@qq.com
# @File : tkinter_excel2fasta.py
# @desc :
import tkinter as tk
# 创建窗口
from tkinter import filedialog
import pandas as pd

root_window = tk.Tk()
# 给窗口起一个名字
root_window.title("excel小工具")
root_window.geometry('800x600')

var = tk.StringVar()
l = tk.Label(root_window, text='', bg='green', font=('Arial', 12), width=800, height=15)
l.pack()

selected_col = []
all_variable=[]

def generateAllCol(checkNum):
    all_variable.append(checkNum)




def add_column(column,checkV):
    state = checkV.get()
    print(state)
    if state == 1:
        selected_col.append(column)


def print_selection():
    l.config(text='You have selected ' + var.get())


def sequence_choose():
    print(all_variable)
    for key_val_col in set(all_variable):
        for key in key_val_col.keys():
            if key_val_col[key]==1:
                c = tk.Radiobutton(root_window, text=key,
                                   command=print_selection, variable=var, value=key_val_col[key]
                                   ).pack(side='left')


def excute(file_path):

    if file_path.endswith('xls') or file_path.endswith('xlsx'):
        global data

        data = pd.read_excel(file_path)
        number = 0
        for column in data.columns:
            number += 1
            if number <= 5:
                checkNum={}
                c = tk.Checkbutton(root_window, text=column, onvalue={number:1}, offvalue={number:0}
                                   , variable=checkNum,command='generateAllCol(checkNum)').place(x=number * 200, y=100, width=200, height=30)

            elif 5 < number < 11:
                checkV = tk.IntVar()
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkNum).place(x=(number - 5) * 200, y=145, width=200, height=30)
            elif 11 <= number < 16:
                checkV = tk.IntVar()
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkNum).place(x=(number - 10) * 200, y=190, width=200, height=30)
            else:
                checkV = tk.IntVar()
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkNum).place(x=(number - 15) * 200, y=235, width=200, height=30)
        b3 = tk.Button(root_window, text='选择序列', width=15, height=2, command=sequence_choose)

        b3.pack(side='left', anchor='nw')

        # l2 = tk.Label(root_window, text='选择序列', bg='green', width=50, font=('Arial', 12), height=15)
        # l2.pack()
        # l3 = tk.Label(root_window, text='', bg='green', width=50,font=('Arial', 12), height=15)
        # l3.pack(side='left')


def openfile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(
         ("excel", "*.xlsx"), ("excel", "*.xls"),("csv", "*.csv")))
    excute(file_path)


b1 = tk.Button(root_window, text='打开文件', width=10, height=2, command=openfile)
b1.place(x=40, y=40)

b2 = tk.Button(root_window, text='执行', width=10, height=2, command=openfile)
b2.place(x=150, y=40)

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
