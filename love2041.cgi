#!/usr/bin/python
import os
import cgitb
from lib.dataparser import DataParser
from lib.template import TEngine
from lib.config import HTML_HEADER
from lib.config import PAGESIZE
from lib.config import WEBDIR
from lib.helper import make_walk_data_list
from lib.helper import make_person_content
from lib.helper import show_header
from lib.helper import check_login
from lib.request import Request
from lib.request import Request

cgitb.enable()
request = Request()

if not check_login():
    request.redirect("user_login.cgi")

query_dict = request.get_query_dict()
nowpage = query_dict.get("page", 1)
    
DATAINFO = make_walk_data_list()
PAGECOUNT = len(DATAINFO) / PAGESIZE + 1 if len(DATAINFO) % PAGESIZE > 0 else len(DATAINFO) / PAGESIZE
show_header()
content = make_person_content(DATAINFO, nowpage, PAGECOUNT)
engine = TEngine("index.html", dict(server_addr=WEBDIR, content=content, page_up=str(int(nowpage) - 1), page_down=str(int(nowpage) - 1)), header=False)
engine.show()
