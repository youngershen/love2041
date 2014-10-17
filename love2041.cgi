#!/usr/bin/env python
import os
import cgitb
from lib.dataparser import DataParser
from lib.template import TEngine
from lib.config import HTML_HEADER
from lib.helper import make_walk_data_list
from lib.helper import make_person_content
from lib.helper import show_header

DATAINFO = make_walk_data_list()
cgitb.enable()
show_header()
print make_person_content(DATAINFO)
