#!/usr/bin/python
import os
import cgitb

from lib.request import Request
from lib.template import TEngine
from lib.helper import make_walk_data_list
from lib.helper import get_full_data
from lib.helper import query_userinfo
from lib.helper import show_header

cgitb.enable()

show_header()
request = Request()
USERDATA = get_full_data()
query_dict = request.get_query_dict()
username = query_dict.get('username', None)

if request.method() == 'GET':

    if username is None:
        pass
    else:
        userinfo =  query_userinfo(username)
        #print userinfo
        engine = TEngine("person_info.html", userinfo, False)
        engine.show()
else:
    pass
    
