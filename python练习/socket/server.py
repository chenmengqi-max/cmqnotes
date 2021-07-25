"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/7/3 - 18:25
"""
from socket import *
IP = ''
PORT = 50000   # 端口号
BUFLEN = 512 # 定义一次从socket缓冲区最多读入512个字节数据

""" 实例化一个socket对象
    参数一表示该socket网络层使用ip协议
    参数二表示传输层使用tcp协议
"""
listenSocket = socket(AF_INET,SOCK_STREAM)
listenSocket.bind((IP,PORT)) # 绑定地址和端口

# 使socket处于监听状态，等待客户端的连接请求
# 参数5表示最多接受5个等待连接的客户端
listenSocket.listen(5)
print(f"服务器启动成功，在{PORT}端口等待客户端连接···")

"""
accept返回一个元组，一个新的套接字来和客户端通信，addr保存了客户端的ip地址和端口号
后面和客户端通信时，要使用这个新生成的套接字，而不是原来服务器端的套接字。
accept() 会阻塞程序执行（后面代码不能被执行），直到有新的请求到来。
"""
dataSocket,addr = listenSocket.accept()

print("接受一个客户端连接：" ,dataSocket,addr)

while True:

    recved = dataSocket.recv(BUFLEN) # 读取对方发送的请求，BUFLEN指定从接收缓存里最多读取多少字节

    info = recved.decode()  # 读取的自己而数据是bytes类型，需要解码
    print(f"服务端收到了客户端信息:{info}")

    dataSocket.send(f'服务端发送给客户端信息'.encode( ))
    # 如果返回空bytes，表示对方关闭了链接
    if not recved:
        print("客户发来空信息")
        break

dataSocket.close()
listenSocket.close()
