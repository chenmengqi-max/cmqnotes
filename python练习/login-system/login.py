from tkinter import *

import json
from tkinter import messagebox

"""注意每次全部用户集合都要从文件里先读"""
file = open('userdate.txt','r')
js = file.read()
userdate = json.loads(js)
nowuser=""
login = Tk()
login.title('Login') #定义窗口名称
login.geometry('210x150')  #定义窗口尺寸
Label(login,text='用户登录').grid(row=0,column=0,columnspan=2) #第三个属性为组件的列宽

Label(login,text='用户名：').grid(row=1,column=0)
name = Entry(login)
name.grid(row=1,column=1) #用户名输入框所在行列

Label(login,text='密码：').grid(row=2,column=0,sticky=E) # E代表右对齐
passwd = Entry(login,show='*') # 密码显示为*
passwd.grid(row=2,column=1)

def successful():
    user = {name.get(): passwd.get()}
    print('user:', name.get())
    file = open('userdate.txt','r')
    js = file.read()
    dic = json.loads(js)
    # if name.get() == 'admin' and passwd.get() == 'admin':
    for key in user:
        if (key in dic) and user[key]==dic[key]:
            messagebox.showinfo(title='successful', message='登录成功')
            global nowuser
            nowuser = name.get()
            login.destroy()
        else:
            messagebox.showerror(title='wrong',message='登录失败，用户名或密码错误')
Button(login,text='登录',command=successful).grid(row=3,column=0,columnspan=2)


def registereds():
    registered = Tk()
    registered.title('registered')
    registered.geometry('230x185')
    Label(registered,text='用户注册').grid(row=0,column=0,columnspan=2)

    Label(registered,text='用户名：').grid(row=1,column=0,sticky=E)
    names = Entry(registered)
    names.grid(row=1,column=1)

    Label(registered,text='密码：').grid(row=2,column=0,sticky=E)
    passwds = Entry(registered,show='*')
    passwds.grid(row=2,column=1)

    Label(registered,text='确认密码：').grid(row=3,column=0)
    repasswd = Entry(registered,show='*')
    repasswd.grid(row=3,column=1)


    def registeredes():
        if not (any([x.isdigit() for x in names.get()]) and any([x.isalpha() for x in names.get()])):
            messagebox.showerror(title='wrong',message='注册失败，用户名格式错误，必须包括字母和数字')
        # elif len(passwds.get()) < 8:
        #     messagebox.showerror(title='wrong',message='注册失败，密码不应少于8位')
        elif passwds.get() != repasswd.get():
            messagebox.showerror(title='wrong',message='注册失败，两次密码不相同')
        else:
            messagebox.showinfo(title='successful',message='注册成功！欢迎您。新用户')
            userdate[names.get()]=passwds.get()
            js = json.dumps(userdate)
            file = open('userdate.txt','w')
            file.write(js)
            file.close()


    Button(registered,text='注册',command=registeredes).grid(row=6,column=0,columnspan=2)
Button(login,text='还没有用户？点击注册！',command=registereds).grid(row=4,column=0,columnspan=2)
login.mainloop()
