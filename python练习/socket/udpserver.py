#-*- coding: utf-8 -*-
#@Time : 2021/3/27 17:35
#@Author : HUGBOY
#@File : UDPServer.py
#@Software: PyCharm

from socket import *

HOST = '127.0.0.1'
PORT = 666

s = socket(AF_INET, SOCK_DGRAM)

s.bind((HOST, PORT))

print('...Waiting for message...')

while True:
    data, address = s.recvfrom(1024)
    print('Accept message:' + data.decode(),address)
    Reply = input('Send message:')
    s.sendto(Reply.encode(),address)
s.close()