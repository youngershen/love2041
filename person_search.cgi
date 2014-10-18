#!/usr/bin/python
import os
from urllib2 import urlparse
import cgitb

from lib.request import Request
from lib.config import WEBDIR
from lib.config import HTML_HEADER
from lib.helper import make_walk_data_list
from lib.helper import get_full_data
from lib.helper import query_userinfo
from lib.helper import show_header
from lib.helper import search_by_name
from lib.helper import make_person_content
from lib.helper import search_person_content

from lib.template import TEngine
cgitb.enable()

request = Request()


if request.method() == "GET":
    query_dict = request.get_query_dict()

    print HTML_HEADER
    result = search_by_name(urlparse.unquote(query_dict.get("name","")))
    
    nowpage = query_dict.get("page", 1)
    context = dict()
    content = search_person_content(result, nowpage, 1)
    if len(content) == 0:
        content = "result not found"
    context['content'] = content
    context['server_addr'] = WEBDIR
    engine = TEngine("search_info.html", context, False)
    engine.show()
else:
    print "method not allowed"

