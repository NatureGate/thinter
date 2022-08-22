# @Time : 2022/8/14 10:58
# @Author : 龙锐 942121483@qq.com
# @File : tkinter_excel2fasta.py
# @desc :
import tkinter as tk
# 创建窗口
from tkinter import filedialog
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root_window = ttk.Window(themename="flatly")

# 给窗口起一个名字
root_window.title("耿阳的excel小工具")
root_window.geometry('800x600')

var = tk.StringVar()
l = ttk.Label(root_window, text='', bootstyle="danger")
l.pack()

duplicate_gene_col_name = tk.StringVar()
duplicate_gene_id = tk.StringVar()
selected_col = []
column_names = []
all_variable = []


def add_duplicate_col():
    duplicate_gene_col_name.get()


def execute_file():
    l2 = ttk.Label(root_window, text='文件生成中.....', bootstyle="success")
    l2.place(relx=0.4, rely=0.7)
    gene_pro_col = var.get()
    print(gene_pro_col)
    noduplicate_col = set(selected_col)
    print(noduplicate_col)
    noduplicate_col.remove(gene_pro_col)
    data['new_name'] = ""
    flag = True
    for col in noduplicate_col:
        if flag:
            data['new_name'] = data[col].map(str)
            flag = False
        else:
            data['new_name'] = data['new_name'].map(str) + "-" + data[col].map(str)
    endpoint = file_path.rindex(".")
    file_path_new = file_path[0:endpoint] + ".fasta"
    new_data = data[['new_name', gene_pro_col]]
    with open(file_path_new, 'a+') as f:
        for i in range(new_data.shape[0]):
            f.write(">" + str(new_data.iloc[i, 0]))
            f.write("\n")
            f.write(str(new_data.iloc[i, 1]))
            f.write("\n")
    l2.config(text='文件已创建，请关闭窗口')


def print_selection():
    l.config(text='You have selected ' + var.get())


def sequence_choose():
    count = 0
    for i in range(all_variable.__len__()):

        if all_variable[i].get() == 1:
            count = count + 1
            selected_col.append(column_names[i])
            r2 = ttk.Radiobutton(root_window, text=column_names[i], variable=var, value=column_names[i],
                                 command=execute_file)
            r2.place(x=40 + count * 150, y=upheight + 100)
            print(column_names[i], count)


def excute(file_path):
    if file_path.endswith('xls') or file_path.endswith('xlsx'):
        global data
        data = pd.read_excel(file_path)
        number = 0
        # print(column_names)
        for column in data.columns:
            column_names.append(column)
            number += 1
            checkV = tk.IntVar()
            if number <= 5:
                c = ttk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                    , variable=checkV)
                c.place(x=number * 200, y=100, width=200, height=30)
                # c.pack()
            elif 5 < number < 11:
                c = ttk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                    , variable=checkV)
                c.place(x=(number - 5) * 200, y=145, width=200, height=30)

            elif 11 <= number < 16:
                c = ttk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                    , variable=checkV)
                c.place(x=(number - 10) * 200, y=190, width=200, height=30)

            elif 16 <= number < 21:
                c = ttk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                    , variable=checkV)
                c.place(x=(number - 15) * 200, y=235, width=200, height=30)

            else:
                c = ttk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                    , variable=checkV)
                c.place(x=(number - 20) * 200, y=280, width=200, height=30)

            all_variable.append(checkV)
        global upheight
        upheight = 100 + (number / 5) * 45 + 20
        print(upheight)
        b3 = ttk.Button(root_window, text='选择序列', bootstyle=SUCCESS, command=sequence_choose)
        b3.place(x=40, y=100 + (number / 5) * 45 + 20)

        # l2 = tk.Label(root_window, text='选择序列', bg='green', width=50, font=('Arial', 12), height=15)
        # l2.pack()
        # l3 = tk.Label(root_window, text='', bg='green', width=50,font=('Arial', 12), height=15)
        # l3.pack(side='left')


def openfile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(
        ("excel", "*.xlsx"), ("excel", "*.xls"), ("csv", "*.csv")))
    excute(file_path)


def open_file_du():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(
        ("excel", "*.xlsx"), ("excel", "*.xls"), ("csv", "*.csv")))
    data = pd.read_excel(file_path)
    number = 0
    l3 = ttk.Label(root_window, text='选择需要去重的列').place(relx=0.4, y=100)
    l4 = ttk.Label(root_window, text='选择ID列').place(relx=0.6, y=100)
    for column in data.columns:
        number += 1
        if number <= 4:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=number * 180, y=130)
        elif 4 < number <= 8:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 4) * 180, y=175)
        elif 8 < number <= 12:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 8) * 180, y=220)
        elif 12 < number <= 16:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 12) * 180, y=265)
        elif 16 < number <= 20:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 16) * 180, y=310)
        elif 20 < number <= 24:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 20) * 180, y=355)
        else:
            r = ttk.Radiobutton(root_window, text=column, variable=duplicate_gene_col_name, value=column,
                                command=add_duplicate_col).place(x=(number - 24) * 180, y=400)


b1 = ttk.Button(root_window, text='打开文件', bootstyle=SUCCESS, command=openfile)
b1.place(x=40, y=40)
# b1.pack()

b2 = ttk.Button(root_window, text='单表去重', bootstyle=SUCCESS, command=open_file_du)
b2.place(x=150, y=40)
# b2.pack()

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
