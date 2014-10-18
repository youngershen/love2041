#!/usr/bin/python
import os
import cgitb
import cgi
from lib.request import Request
from lib.template import TEngine
from lib.config import WEBDIR
from lib.config import HTML_HEADER
from lib.helper import check_login
from lib.helper import do_login

cgitb.enable()

request = Request()

#handler post
#form = cgi.FieldStorage() 

user_login_temp = TEngine("user_login.html", dict(name="test"), header=False)
engine = TEngine("user_login.html", dict(server_addr=WEBDIR),  True)
if request.method() =='POST':
    form = cgi.FieldStorage()
    username = form.getvalue("username")
    password = form.getvalue("password")
    if do_login(username, password):
        request.login_and_direct([dict(username=username), dict(password=password)], "love2041.cgi")
    else:
        engine.show()
else:
    #username = request.get_post("username")
    
    if check_login():
        request.redirect("love2041.cgi")
    else:
        user_login_temp = TEngine("user_login.html", dict(name="test"), header=False)
        engine = TEngine("user_login.html", dict(server_addr=WEBDIR),  True)
        engine.show()
        #print HTML_HEADER
        #print username
        #print check_login()
        #engine.show()
