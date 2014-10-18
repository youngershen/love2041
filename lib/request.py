#!/usr/bin/python
#-*- coding: utf-8 -*-

#HTTP_COOKIE
#VERSIONER_PYTHON_PREFER_32_BIT
#SERVER_SOFTWARE
#SCRIPT_NAME
#SERVER_SIGNATURE
#REQUEST_METHOD
#SERVER_PROTOCOL
#QUERY_STRING
#PATH
#HTTP_USER_AGENT
#HTTP_CONNECTION
#SERVER_NAME
#REMOTE_ADDR
#SERVER_PORT
#SERVER_ADDR
#DOCUMENT_ROOT
#SCRIPT_FILENAME
#SERVER_ADMIN
#HTTP_HOST
#HTTP_CACHE_CONTROL
#REQUEST_URI
#HTTP_ACCEPT
#GATEWAY_INTERFACE
#REMOTE_PORT
#HTTP_ACCEPT_LANGUAGE
#__CF_USER_TEXT_ENCODING
#VERSIONER_PYTHON_VERSION
#HTTP_ACCEPT_ENCODING

import os
import cgi
from config import HTML_HEADER

SET_COOKIES_TP = "Set-Cookie:{key}={value};\r\n"

def cookie_helper(cookie):
    return "Set-Cookie:{key}={value};\r\n".format(key=cookie.keys()[0],value=cookie.values()[0])

def set_http_cookie(cookies):
    header = ""
    for cookie in cookies:
        header += cookie

    #header += HTML_HEADER
    print header
    

def strip(var):
    return var.strip()
class Request(object):
    def __init__(self):
        self.environ = os.environ

    def method(self):
        #return self.environ['REQUEST_METHOD']
        return os.environ['REQUEST_METHOD']
    def get_query_dict(self):
        if self.method() == 'GET':
            query_str = self.environ['QUERY_STRING']
            kv = query_str.split("&")
            query_dict = dict()
            for v in kv:
                ret = v.split("=")
                if len(ret) > 1:
                    query_dict[ret[0]] = ret[1]

            return query_dict
        else:       
            return "request do not use GET method"

    def get_post(self, key):
        form = cgi.FieldStorage()
        return form.get_value(key)

    def get_cookie(self):
        cookies = self.environ.get('HTTP_COOKIE', None)
        cookie_dict = dict()
        if cookies is not None:
            for cookie in map(strip, cookies.split(";")):
                (key, value) = cookie.split("=")
                cookie_dict[key] = value
        return cookie_dict

    def set_cookie(self, context):
        #context is a list contains dict as key->value
        #[ {key:value} ...]
        cookie_list = []
        for item in context:
            cookie = cookie_helper(item)
            cookie_list.append(cookie)

        set_http_cookie(cookie_list)
        
    def login_and_direct(self,context, url):
        cookies_list = []
        for item in context:
            cookie = cookie_helper(item)
            cookies_list.append(cookie)
        cookies_list.append("Location: {url}\r\n".format(url=url))
        set_http_cookie(cookies_list)



    def redirect(self, url):
        print "Location: {url}\r\n".format(url=url)
