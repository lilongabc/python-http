#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/8
import urllib2
#urllib 在python 3中被修改为urllib.request
#urlopen向指定的url发送请求，返回服务器相应的类文件对象，类似文件的对象，有read,write,readlin
#也支持一些响应的文件比如getcod（）
#urlopen 不支持构造url请求，也就是不支持构造head等。 /最好写上要不会出错。
response = urllib2.urlopen('http://www.holyzone.com.cn/')
#服务器返回的类文件对象，支持python文件对象的操作方法
#比如read()方法是读取文件里的全部内容，返回字符串
html = response.read()
#打印响应内容
print html
