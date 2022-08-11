import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var = tk.StringVar()
e = tk.Entry(root_window,show=None)
e.pack()

on_hit = True
def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert(0.0,var)


b1 = tk.Button(root_window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(root_window,text='insert end',command=insert_end)
b2.pack()

t = tk.Text(root_window,height=2)
t.pack()
#开启主循环，让窗口处于显示状态
root_window.mainloop()