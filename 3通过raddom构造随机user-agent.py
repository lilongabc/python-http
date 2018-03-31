#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/3/11
#通过构造随机的http head user-agent,来进行反反爬虫

import urllib2
import random
#构造随机user agent 列表
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/6.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/7.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/8.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
]
#随机选择user agent 在列表中并输出查看
user_agent = random.choice(ua_list)
print user_agent
#构造请求并插入选择好的user_agent
#构造一个http请求
request = urllib2.Request("http://www.holyzone.com.cn/")
request.add_header("User-agent",user_agent)
#开始请求并实例化给response
response = urllib2.urlopen(request)
# get_header()获取一个已有的http头的值，注意只能使第一个字母大写，其余都是小写
print request.get_header("User-agent")

