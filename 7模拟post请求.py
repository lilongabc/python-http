#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/31
'''
Get 请求：查询参数在RUL QueryString里保存
Post 请求：查询参数在Body Form表单里保存
'''

import urllib
import urllib2

url ="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
key = raw_input("plase input you want translate words: ")
headers = {
    "Host": "fanyi.youdao.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":"http://fanyi.youdao.com",
    "Pragma":"no-cache",
    "Referer":"http://fanyi.youdao.com/",
    "X-Requested-With":"XMLHttpRequest",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

formdata = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1522508661368",
    "sign":"510ee0126b1de7305480db43c0ed08a7",
    "doctype":"json",
    "version":"2.1",
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_CLICKBUTTION",
    "typoResult" : "false"
}
#通过rulencode把翻译的中文内容尽心rul转码。
data = urllib.urlencode(formdata)
print data
#构造请求
request = urllib2.Request(url,data=data,headers=headers)

html =  urllib2.urlopen(request)
print html.read()