#!/usr/bin/env python
# -*- coding:utf-8 -*-  

import os
import re
from config import HTML_HEADER
from config import TEMPLATEDIR
from config import HTML_STOKEN as STOKEN
from config import HTML_ETOKEN as ETOKEN
from helper import filter_list_space
from helper import parse_list_to_html

REG_CONTENT = "(?<="+ STOKEN +")[^{}]*(?="+ ETOKEN+")"

class TEngine(object):
    def __init__(self, filename, context, header = True):
        self.filename = TEMPLATEDIR +  filename
        self.context = context
        self.is_header = header
        self.load()
    def load(self):
        try:
            with open(self.filename) as file:
                if self.is_header:
                    content = HTML_HEADER + file.read()
                else:
                    content = file.read()
        except IOError as e:
            print self.filename
        else:
            self.content = content
     
    def show(self):
        self.parse()
        print self.content

    def parse(self):
        
        content_key = filter_list_space(re.findall(REG_CONTENT, self.content))
        if self.context is not None:
            for item in self.context.items():
                if item[0] in content_key:
                    self.content = self.content.replace(STOKEN + item[0] + ETOKEN, parse_list_to_html(item[1]))

                else:
                    pass
