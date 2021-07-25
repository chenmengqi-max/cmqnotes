"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/7/18 - 22:44
"""
#-*- coding: utf-8 -*-
#@Time : 2021/3/27 17:30
#@Author : HUGBOY
#@File : UDPClient.py
#@Software: PyCharm

from socket import *

HOST = '127.0.0.1'
PORT = 666

address = (HOST, PORT)
s = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Send message:')
    s.sendto(message.encode(), address)
    data,addr = s.recvfrom(1024)
    print(data.decode(),addr)

s.close()
