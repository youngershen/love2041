#!/usr/bin/python
# -*- coding:utf-8 -*-  

import os

HTML_HEADER = "Content-type: text/html\r\n\r\n"
DATADIR = os.getcwd() + "../data/students/"
TEMPLATEDIR = os.getcwd() + "/template/"
IMGTYPE = ['png', 'jpg', 'jpeg', 'gif','bmp']

WEBDIR = "/cgi-bin/love2041/"
HTML_STOKEN = "{{"
HTML_ETOKEN = "}}"

DATADIR = os.getcwd() +  "/data/students/"
PAGESIZE = 10
