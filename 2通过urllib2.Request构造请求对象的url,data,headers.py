#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/11

import urllib2
#head 是字典类型,必须要写user-agent为了反防爬虫，accep-enconding不要写，避免服务器返回内容是压缩过的内容。
my_headers = {
    "Host":"www.holyzone.com.cn",
    "Connection": "keep-alive",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "User-Agent":" Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
#通过urllib2的request 方法构造请求对象,url ,data headers 参数是有顺序的，所以要写函数名
request = urllib2.Request('http://www.holyzone.com.cn/',headers=my_headers)
resopnse = urllib2.urlopen(request)
#html = resopnse.getcode() 返回http code
#html = resopnse.geturl() 输出为返回页面的具体是哪个url，为了判断返回页面是否为跳转后的url.
#html = response.info() 返回http header response infomaation
html = resopnse.read()
print html


'''
GET / HTTP/1.1
Host: www.holyzone.com.cn
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
If-None-Match: "b2dcc63abb7d31:0"
If-Modified-Since: Fri, 09 Mar 2018 13:32:05 GMT
'''