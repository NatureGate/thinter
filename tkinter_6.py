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
    if var1.get()==1 and var2.get()==1:
        l.config(text='I love both')
    elif var1.get()==1 and var2.get()==0:
        l.config(text='I love Python')
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text='I love C++')
    elif var1.get() == 0 and var2.get() == 0:
        l.config(text='I dont love either')
var1 = tk.IntVar()
var2 = tk.IntVar()
c1= tk.Checkbutton(root_window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2= tk.Checkbutton(root_window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()

#开启主循环，让窗口处于显示状态
root_window.mainloop()

