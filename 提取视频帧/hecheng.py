"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/2/21 - 17:29
"""
import cv2
import os
import random

img = cv2.imread('sibiaoqing/1.jpg')  #读取第一张图片
fps = 60
imgInfo = img.shape
size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
print(size)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
videoWrite = cv2.VideoWriter('output1.mp4',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
#videoWrite = cv2.VideoWriter('0.mp4',fourcc,fps,(1920,1080))

files = os.listdir('sibiaoqing/')
out_num = len(files)
for i in range(0,out_num):
    fileName = 'sibiaoqing/'+str(i)+'.jpg'    #循环读取所有的图片,假设以数字顺序命名
    img = cv2.imread(fileName)

    videoWrite.write(img)# 将图片写入所创建的视频对象