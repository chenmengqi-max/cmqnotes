"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/3/26 - 9:47
"""
import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("https://www.bilibili.com")
# file = open("test1.html","w")
# contents = response.read().decode('utf-8')
# file.write(contents) #对获取到的网页源码进行解码

#获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"123456":"789456"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#提取内容
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheaders())#拿所有的就是加s
# print(response.getheader("Server"))#提取单个的不加s

#伪装成浏览器（post方式）
# import urllib.parse
# url = "https://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#               "AppleWebKit/537.36 (KHTML, like Gecko) "
#               "Chrome/89.0.4389.90 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url = url,data = data ,headers = headers ,method = "POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#访问douban（get方式）
url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/89.0.4389.90 Safari/537.36"
}
req = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))