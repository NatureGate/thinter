import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var = tk.StringVar()
l = tk.Label(root_window,textvariable=var,bg='green',font=('Arial',12),width=800,height=15)
l.pack()
on_hit = True
def hit_me():
    global on_hit
    if on_hit:
        on_hit = False
        var.set('you hit me')
    else:
        on_hit = True
        var.set('')


b = tk.Button(root_window,text='hit me',width=15,height=2,command=hit_me)
b.pack()
#开启主循环，让窗口处于显示状态
root_window.mainloop()