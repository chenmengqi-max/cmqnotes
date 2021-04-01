"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/3/27 - 14:01
"""
import urllib.request
def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影top250.xls"
    # 3.保存数据
    #saveData(savepath)

    askURL("https://movie.douban.com/top250?start=0")





def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用获取页面信息的函数，10次，一共250条
        url = baseurl + str(i*25)
        html = askURL((url)) #保存获取到的网页源码
    #2.逐一解析数据

    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    #用户代理表示告诉豆瓣服务器，我们是什么类型的机器，可以接受什么水平的信息。
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.90Safari / 537.36"
    }
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



#3.保存数据
def saveData(savepath):
    pass

if __name__ == '__main__':
    main()