"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/7/3 - 18:25
"""
from socket import *
IP = '127.0.0.1'
SERVER_PORT = 50000
BUFLEN = 512

dataSocket = socket(AF_INET,SOCK_STREAM)

dataSocket.connect((IP,SERVER_PORT))

while True:

    tosend = input("请输入要发送的信息：")
    dataSocket.send(tosend.encode()) # 发送消息，编码为bytes
    recved = dataSocket.recv(BUFLEN) # 等待接收服务器端的消息
    print("客户端接收到消息：",recved.decode())
    if tosend == 'exit':
        print("客户端退出")
        break
    if not recved:
        print("客户端未接受到消息，退出")
        break
    if recved == '\n':
        print("客户端未接受到消息，退出")
        break

dataSocket.close()
