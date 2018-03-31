#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/12
'''
urllib的urlencode()接受的参数是一个字典。
urllib 仅仅可以接受URL，不能创建设置了Headers的Request类实例。
但是urllib提供urlencode方法用来Get查询字符串的产生，而urllib2则没有。（这是urllib和rullib2经常一起使用的主要原因）
编码工作使用urllib的urlencode()函数。帮我们将 key:value这样的建值对转换成“key=value”这样的字符串，解码工作可以使用urllib的unquote()函数。
注意不是urllib2.urlencode()
urllib仅可以接收rul,不能构建headers的request实例，一般用于urlencode,所以需要和rullib2结合使用。
'''
#只要是进行url编码，就用到urllib，其它的时候用urllib2就可以了
import urllib

url = "http://www.baidu.com/s?"
#为什么要用字典类型？因为urllib.urlencode只支持字典类型，他会把地点中的：号编程=号
#服务器在参数传输的时候，必须说汉字是通过url编码传输的，所以要通过rullib.rulencode转成url编码
wd = {"wd":"力尊信通李龙"}

myurlencode = urllib.urlencode(wd)
#中文字符转urlenocde   wd=%E5%8A%9B%E5%B0%8A%E4%BF%A1%E9%80%9A%E6%9D%8E%E9%BE%99
print myurlencode
#转换回中文输出为 wd=力尊信通李龙
print urllib.unquote(myurlencode)



