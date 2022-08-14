import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var = tk.StringVar()
l = tk.Label(root_window,text='',bg='green',font=('Arial',12),width=800,height=15)
l.pack()

def print_selection(number):
    l.config(text='You have selected '+number)
s = tk.Scale(root_window,label='try me',from_=5,to=11,orient = tk.HORIZONTAL,length = 200,
             showvalue=0,tickinterval=3,resolution=0.1,command=print_selection)
s.pack()




#开启主循环，让窗口处于显示状态
root_window.mainloop()