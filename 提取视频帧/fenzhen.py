"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/2/20 - 19:54
"""
import cv2

vc = cv2.VideoCapture('sibiaoqing.mp4')  # 读入视频文件，命名cv
n = 1  # 计数

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False

timeF = 1  # 视频帧计数间隔频率

i = 0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite('sibiaoqing/{}.jpg'.format(i), frame)  # 存储为图像
    n = n + 1
    cv2.waitKey(1)
vc.release()
