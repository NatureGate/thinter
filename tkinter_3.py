import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var1 = tk.StringVar()

l = tk.Label(root_window,textvariable=var1,bg='green',font=('Arial',12),width=800,height=15)
l.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(root_window)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()
def insert_label():
    value = lb.get(lb.curselection())
    var1.set(value)



b1 = tk.Button(root_window,text='print selection',width=15,height=2,command=insert_label)
b1.pack()




#开启主循环，让窗口处于显示状态
root_window.mainloop()