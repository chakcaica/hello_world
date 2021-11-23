import tkinter as tk
window = tk.Tk()
screen_width = window.winfo_screenwidth()
srceen_height = window.winfo_screenheight()
x = (screen_width - 200)/2
y = (srceen_height - 100)/2
window.geometry('220x200+%d+%d'%(x,y))
window.title('用户注册')
#读取图片文件
# logo = tk.PhotoImage(file="9/image_logo.jpg")
# icon_login = tk.PhotoImage(file="login.jpg")
# icon_cancel = tk.PhotoImage(file="cancel.jpg")
#在左侧放置一个标签，显示logo图片
# tk.Label(window,justify=tk.LEFT,image=logo).grid(row=0,column=0,rowspan=2)
#放置两个标签，一个为'账户'，一个为'密码'，字体：微软雅黑，12号
tk.Label(window,text='用户注册',font=('Microsoft YaHei',12),anchor=tk.E,padx=50).grid(row=0,column=2,sticky=tk.E)
tk.Label(window,text='学号',font=('Microsoft YaHei',12),anchor=tk.E).grid(row=1,column=1,sticky=tk.E)
tk.Label(window,text='姓名',font=('Microsoft YaHei',12),anchor=tk.E).grid(row=2,column=1,sticky=tk.E)
tk.Label(window,text='性别',font=('Microsoft YaHei',12),anchor=tk.E).grid(row=3,column=1,sticky=tk.E)
tk.Label(window,text='班级',font=('Microsoft YaHei',12),anchor=tk.E).grid(row=4,column=1,sticky=tk.E)
tk.Label(window,text='电话',font=('Microsoft YaHei',12),anchor=tk.E).grid(row=5,column=1,sticky=tk.E)
#在标签的右侧放置输入控件  
var_usr_users = tk.StringVar()                                                                                                                                                                             
var_usr_stuNu = tk.StringVar()
var_usr_name = tk.StringVar()
var_usr_sex = tk.StringVar()
var_usr_class = tk.StringVar()
var_usr_phone = tk.StringVar()
tk.Entry(window,width = 15,textvariable=var_usr_stuNu).grid(row=1,column=2)
tk.Entry(window,width = 15,textvariable=var_usr_name).grid(row=2,column=2)
tk.Entry(window,width = 15,textvariable=var_usr_sex).grid(row=3,column=2)
tk.Entry(window,width = 15,textvariable=var_usr_class).grid(row=4,column=2)
tk.Entry(window,width = 15,textvariable=var_usr_phone).grid(row=5,column=2)
#创建放置按钮的框架控件
frame = tk.Frame(window,bg='white',width=200,height=35,padx=2,pady=2)
frame.grid(row=6,column=1,columnspan=2,sticky=tk.W)
#定义"注册"按钮的回调函数
def login():
    psw = var_usr_stuNu.get()
    user = var_usr_name.get()
    sex = var_usr_sex.get()
    clas = var_usr_class.get()
    phone = var_usr_phone.get()
    if user and psw and sex and clas and phone:
        print("stuNu:%s\nuserName:%s\nsex:%s\nclass:%s\nphone:%s" % (user,psw,sex,clas,phone))
    else:
        print("Please Enter Username and Password!")
#放置两个按钮，一个"注册"，一个"取消"
tk.Button(frame,bg='green',compound=tk.LEFT,text='注册',font=('Microsoft YaHei',11),anchor=tk.E,padx=5,command=login).grid(row=7,column=1,padx=10)
tk.Button(frame,bg='red',compound=tk.LEFT,text='取消',font=('Microsoft YaHei',11),anchor=tk.E,padx=5,command=window.quit).grid(row=7,column=2,padx=6,sticky=tk.E)
#定义菜单回调函数
def callback_hello():
    print("hello from menu!")
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=False)
filemenu.add(itemType='command',label="Open",command=callback_hello)
filemenu.add(itemType='command',label="Save",command=callback_hello)
filemenu.add(itemType='separator')
filemenu.add(itemType='command',label="Exit",command=window.quit)
menubar.add(itemType='cascade',label="File",menu=filemenu,underline=0)
#创建Edit下拉菜单，并添加到菜单栏
editmenu = tk.Menu(menubar,tearoff=False)
editmenu.add(itemType='command',label="Cut",command=callback_hello)
editmenu.add(itemType='command',label="Copy",command=callback_hello)
editmenu.add(itemType='command',label="Paste",command=callback_hello)
menubar.add(itemType='cascade',label="Edit",menu=editmenu,underline=0)
#创建Help下拉菜单，并添加到菜单栏
helpmenu = tk.Menu(menubar,tearoff=False)
helpmenu.add(itemType='command',label="About",command=callback_hello)
menubar.add(itemType='cascade',label="Help",menu=helpmenu)
#显示菜单
window.config(menu=menubar)
#启动TK消息循环
window.mainloop()        
