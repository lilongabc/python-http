#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/12
###未完成
import urllib
import urllib2


def loadPage(url,filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename: 处理的文件名
    """
    print '正在下载' + filename
    headers = {
    "Host": "www.baidu.com",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    request = urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()

def writePage(html,filename):
    """
        作用：将html内容写入到本地
        html: 服务器响应文件内容

    """
    print "Writeing" + filename
    #文件写入
    with open(filename,"w") as f:
        f.write(html)
    print "-"*40
def tiebaSpider(url,beginPage,endPage):
    '''
        作用：贴吧爬虫调度器，负责组合处理每个页面的URL
        URL：贴吧url
        beginPage: Start page
        endPage: end Page
    '''
    for page in range(beginPage,endPage + 1):
        pn = (page - 1 ) * 50
        filename = "No" + str(page) + "page.html"
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        html = loadPage(fullurl,filename)
        #print html
        writePage(html,filename)
if __name__ == "__main__":
    kw = raw_input("请输入要爬取的贴吧名字: ")
    beginPage = int(raw_input("please input start page: "))
    endPage = int(raw_input("please input end page: "))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
