#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1
import urllib2
import ssl
#忽略证书可信，当浏览器提示http站点的证书风险时，忽略继续访问
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'
headers = {
    "Host": "www.12306.cn",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print response.read()
