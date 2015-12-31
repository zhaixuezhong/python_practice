__author__ = 'zxz'

# -- coding: utf-8 --
# coding=utf-8

import urllib3
import sys
import importlib
import brower_request
from bs4 import BeautifulSoup

class CaoLiu:
    importlib.reload(sys)
    print(sys.getdefaultencoding())  # 解决写入文件乱码问题

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = {'User-Agent': self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
        self.BaseUrl = "http://t66y.com/"
        self.j = 1


    #传入某一页的索引获得页面代码
    def getPage(self, i):
        url = 'http://t66y.com/thread0806.php?fid=22&search=&page=' + str(i)
        result =  brower_request.get_html_with_proxy(url)
        return result


    def start(self):
        for i in range(1, 100):  # 设置始末页码
            http = urllib3.PoolManager()
            page = self.getPage(i)
            soup = BeautifulSoup(page, from_encoding="utf8")  #解决BeautifulSoup中文乱码问题
            print("reading page " + str(i))
            # counts = soup.find_all("td", class_="tal f10 y-style")
            counts = soup.find_all("td", { "class" : "tal f10 y-style" })

            for count in counts:
                if int(count.string) > 5:  #选择想要的点击率
                    videoContainer = count.previous_sibling.previous_sibling.previous_sibling.previous_sibling
                    video = videoContainer.find("h3")
                    print("Downloading link " + str(self.j))
                    line1 = (video.get_text())
                    line2 = self.BaseUrl + video.a.get('href')
                    line3 = "view **" + count.string + "** "
                    print(line1)
                    f = open('cao.txt', 'a')
                    f.write(
                        "\n" + "###" + " " + line1 + "\n" + "<" + line2 + ">" + "\n" + line3 + "  " + "page" + str(i) + "\n")
                    f.close()
                    self.j += 1


spider = CaoLiu()
spider.start()