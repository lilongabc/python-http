#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/12


import urllib
import urllib2

url = "http://www.baidu.com/s"

keyword = raw_input("请输入要查询的字符串：")

#编码转换.把raw_input输入的汉字转换成url编码
wd = {"wd" : keyword}
wd = urllib.urlencode(wd)
#构造header
headers = {
    "Host": "www.baidu.com",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
#拼接url
fullurl = url + "?" + wd
#构造请求
requeset = urllib2.Request(fullurl,headers=headers)
#发送请求
response = urllib2.urlopen(requeset)
print response.read()