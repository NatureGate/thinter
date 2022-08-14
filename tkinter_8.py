import tkinter as tk
#创建窗口
root_window = tk.Tk()
#给窗口起一个名字
root_window.title("耿阳的excel小工具")
root_window.geometry('800x600')
var = tk.StringVar()
l = tk.Label(root_window,text='',bg='green',font=('Arial',12),width=800,height=5)
l.pack()

# 下方command参数的do_job函数
counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter += 1


menubar = tk.Menu(root_window)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)
filemenu.add_command(label='保存', command=do_job)
# 分隔线
filemenu.add_separator()
filemenu.add_command(label='退出', command=root_window.quit)

editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='编辑',menu=editmenu)
editmenu.add_command(label='复制',command=do_job)
editmenu.add_command(label='粘贴',command=do_job)

# 在‘文件’下拉菜单中创建二级菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='导入', menu=submenu, underline=0)
submenu.add_command(label='导入图片', command=do_job)
root_window.config(menu=menubar)

#开启主循环，让窗口处于显示状态
root_window.mainloop()

