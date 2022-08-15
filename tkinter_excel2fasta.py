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
column_names = []
all_variable = []

def execute_file():
    l2 = tk.Label(root_window, text='文件生成中.....', bg='green', width=200, font=('Arial', 12), height=15)
    l2.pack()
    gene_pro_col = var.get()
    noduplicate_col = set(selected_col)
    noduplicate_col.remove(gene_pro_col)
    data['new_name'] = ""
    flag = True
    for col in noduplicate_col:
        if flag:
            data['new_name'] = data[col].map(str)
            flag=False
        else:
            data['new_name'] = data['new_name'].map(str) + "-" + data[col].map(str)
    endpoint = file_path.rindex(".")
    file_path_new = file_path[0:endpoint]+".fasta"
    new_data = data[['new_name',gene_pro_col]]
    with open(file_path_new,'a+') as f :
        for i in range(new_data.shape[0]):
            f.write(">"+str(new_data.iloc[i,0]))
            f.write("\n")
            f.write(new_data.iloc[i,1])
            f.write("\n")
    l2.config(text='文件已创建，请关闭窗口')

def print_selection():
    l.config(text='You have selected ' + var.get())


def sequence_choose():
    for i in range(all_variable.__len__()):
        if all_variable[i].get()==1:
            selected_col.append(column_names[i])
            r2 = tk.Radiobutton(root_window, text=column_names[i], variable=var, value=column_names[i], command=execute_file)
            r2.pack()
    print (selected_col)
def excute(file_path):
    if file_path.endswith('xls') or file_path.endswith('xlsx'):
        global data

        data = pd.read_excel(file_path)
        number = 0
        
        #print(column_names)
        for column in data.columns:
            column_names.append(column)
            number += 1
            checkV = tk.IntVar()
            if number <= 5:
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkV)
                c.place(x=number * 200, y=100, width=200, height=30)
            elif 5 < number < 11:
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkV).place(x=(number - 5) * 200, y=145, width=200, height=30)
            elif 11 <= number < 16:
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkV).place(x=(number - 10) * 200, y=190, width=200, height=30)
            else:
                c = tk.Checkbutton(root_window, text=column, onvalue=1, offvalue=0
                                   , variable=checkV).place(x=(number - 15) * 200, y=235, width=200, height=30)
            all_variable.append(checkV)
        b3 = tk.Button(root_window, text='选择序列', width=15, height=2, command=sequence_choose)
        b3.pack(side='left', anchor='nw')

        # l2 = tk.Label(root_window, text='选择序列', bg='green', width=50, font=('Arial', 12), height=15)
        # l2.pack()
        # l3 = tk.Label(root_window, text='', bg='green', width=50,font=('Arial', 12), height=15)
        # l3.pack(side='left')


def openfile():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(
        ("excel", "*.xlsx"), ("excel", "*.xls"), ("csv", "*.csv")))
    excute(file_path)


b1 = tk.Button(root_window, text='打开文件', width=10, height=2, command=openfile)
b1.place(x=40, y=40)

b2 = tk.Button(root_window, text='执行', width=10, height=2, command=openfile)
b2.place(x=150, y=40)

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
