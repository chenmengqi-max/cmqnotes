"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/1/17 - 13:59
"""

import login

Users = [] #存放所有用户的列表
m = 8
class file:
    def __init__(self,filename,e,r,w):
                print("创建失败！当前用户",self.Username,"保存文件数已达上限 ",m)
                print()
        else:
            print("改文件名已存在，请更换文件名")
            print()

    def showfiles(self): #展示该用户对象所包含的所有文件以及权限
        print("当前",self.Username,"用户下文件有：   ")
        for i in self.Userfiles:
            print("  " ,i.Filename,"可执行:",i.E," 可读:",i.R," 可写：",i.W)
        print()
        print()

    def open(self,openfilename,ee,rr,ww):
        if self.exist(openfilename) == 1: #检查是否该文件名已经存在
            if self.Mutex > 0: #确定现在没有别的文件正在打开
                self.Mutex = self.Mutex - 1 #消耗资源量，防止别的文件同时打开
                self.Openqueue.append(openfilename)
                for i in self.Userfiles:
                    if openfilename == i.Filename: #根据本次打开的要求设置二级保护
                        i.EE = ee
                        i.RR = rr
                        i.WW = ww
                print(openfilename,"*****文件已打开*****")
                print()
            else:
                print("有其余文件正在打开，当前文件无法打开！")
                print()
        else:
            print(openfilename,"文件名不存在！")
            print()

    def close(self,closefilename):
        if self.exist(closefilename) == 0: #检查是否该文件名已经存在
            print("文件名不存在！")
            print()
        else:
            if closefilename not in self.Openqueue:
                print("该文件并未打开，无需关闭！")
                print()
            else:
                self.Openqueue.remove(closefilename)
                print(closefilename,"*****文件已关闭*****")
                self.Mutex = self.Mutex + 1

    def exist(self,filename): #检查文件名是否已经在该用户中存在
        for i in self.Userfiles:
            if filename == i.Filename:
                return 1
        return 0

    def delete(self,delfilename):
        if self.exist(delfilename) == 0: #检查是否该文件名已经存在
            print("文件名不存在！")
            print()
        else:
            if delfilename in self.Openqueue:
                self.close(delfilename)#删除之前如果已经打开需要先关闭
            for i in self.Userfiles:
                if i.Filename == delfilename: #遍历到该文件的话则从用户文件列表里删去该文件
                    self.Userfiles.remove(i)
                    print(delfilename,"文件已经删除")
                    self.showfiles()

    def read(self,readfilename):
        if self.exist(readfilename) == 0: #检查是否该文件名已经存在
            print("文件名不存在！")
            print()
        else:
            if readfilename in self.Openqueue:
                for i in self.Userfiles:
                    if readfilename == i.Filename:
                        if i.R ==1 and i.RR == 1:
                            print(readfilename,"文件正在读***")
                            print()
                        else:
                            print(readfilename,"文件不可读***")
                            print()
            else:
                print(readfilename,"文件未打开，请先打开文件")
                print()

    def write(self,writefilename):
        if self.exist(writefilename) == 0: #检查是否该文件名已经存在
            print("文件名不存在！")
            print()
        else:
            if writefilename in self.Openqueue:
                for i in self.Userfiles:
                    if writefilename == i.Filename:
                        if i.W ==1 and i.WW == 1:
                            print(writefilename,"文件正在写***")
                            print()
                        else:
                            print(writefilename,"文件不可写***")
                            print()
            else:
                print(writefilename,"文件未打开，请先打开文件")
                print()

if __name__ == "__main__":
    m = int(input("请输入用户最多可以保存的文件数量："))

    commands = ["creat","delete","open","close","read","write","contents","quit"]
    now_user = User(login.nowuser)  # 获取当前登录的用户名
    print("当前用户为：", login.nowuser,"用户最多可保存文件数量为：",m)
    Users.append(now_user)

    while 1:
        print("当前可执行命令：1.creat  2.delete  3.open  4.close  5.read  6.write  7.contents  8.quit")
        nowcommand =input("请输入当前需要执行的命令")
        if nowcommand not in commands:
            print("请输入正确的指令!")
            print()
        else:
            if nowcommand == "creat":
                newfilename = input("请输入新文件名：")
                e = int(input("请输入执行权限"))
                r = int(input("请输入可读权限"))
                w = int(input("请输入可写权限"))
                now_user.creat(newfilename,e,r,w)

            elif nowcommand == "delete":
                delfilename = input("请输入要删除的文件名：")
                now_user.delete(delfilename)

            elif nowcommand == "open":
                openfilename = input("请输入需要打开的文件名：")
                ee = int(input("请输入执行权限"))
                rr = int(input("请输入可读权限"))
                ww = int(input("请输入可写权限"))
                now_user.open(openfilename,ee,rr,ww)

            elif nowcommand == "close":
                closefilename = input("请输入需要关闭的文件名：")
                now_user.close(closefilename)

            elif nowcommand == "read":
                readfilename = input("请输入需要读的文件名：")
                now_user.read(readfilename)

            elif nowcommand == "write":
                writefilename = input("请输入需要写的文件名")
                now_user.write(writefilename)

            elif nowcommand == "contents":
                now_user.showfiles()

            elif nowcommand == "quit":
                exit(0)



