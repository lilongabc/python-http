#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1
# vm 172.16.0.30 username:python password:python
import urllib
import urllib2
import cookielib
#Cookejar()类构建一个对象来保存cookie的值
cookie = cookielib.CookieJar()
#通过HTTPCookieProcessor（）处理器构建一个处理器对象，用来处理cookie
#参数cookie就是构建CookieJar的对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
#构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)
url = "http://172.16.0.30/user_login.php?"
my_header = {
    "Host": "172.16.0.30",
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
data = "username=python&password=python&action=login"
#第一次是POST请求，发送data内容，获取cookie。
request = urllib2.Request(url,data=data,headers=my_header)
#通过opener发送，而不是urllib2.urlopen(request)，opener 会保存cookie 发送的时候会带上cookie
#生成登录后的cookie
response = opener.open(request)
#print response.read()
#带着cookie 再去get访问页面二，这个页面是登录后的页面。
response_page2 = opener.open("http://172.16.0.30/yourauctions.php")
print response_page2.read()