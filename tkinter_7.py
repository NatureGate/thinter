import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel工具")
root_window.geometry('800x600')
var = tk.StringVar()


canvas = tk.Canvas(root_window,bg='blue',height=400,width=400)
image_file=tk.PhotoImage(file='test.gif')
image = canvas.create_image(10,10,anchor='nw',image=image_file)
x0,y0,x1,y1 = 200,200,300,300
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
arc = canvas.create_arc(x0+50,y0+50,x1+50,y0+50,start=0,extent=90,fill='red')
canvas.pack()
def moveit():
    canvas.move(oval,0,2)
b = tk.Button(root_window,text='move',command=moveit).pack()

#开启主循环，让窗口处于显示状态
root_window.mainloop()

