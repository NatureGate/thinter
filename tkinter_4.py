import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var = tk.StringVar()
l = tk.Label(root_window,text='',bg='green',font=('Arial',12),width=800,height=15)
l.pack()

def print_selection():
    l.config(text='You have selected '+var.get())
r1 = tk.Radiobutton(root_window,text='Option A',variable = var,value='A',command=print_selection)
r1.pack()

r2 = tk.Radiobutton(root_window,text='Option B',variable = var,value='B',command=print_selection)
r2.pack()

r3 = tk.Radiobutton(root_window,text='Option C',variable = var,value='C',command=print_selection)
r3.pack()


#开启主循环，让窗口处于显示状态
root_window.mainloop()