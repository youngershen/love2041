#!/usr/bin/env python
# -*- coding:utf-8 -*-  

import os
import random

from config import DATADIR
from config import HTML_HEADER
from config import WEBDIR
from config import IMGTYPE
from dataparser import DataParser


def show_header():
    print HTML_HEADER
def filter_list_space(rlist):

    nlist = []
    for i in rlist:
        nlist.append(i.strip())
    return nlist

def make_walk_data_list():
    dirlist = os.listdir(DATADIR)
    ret = []
    for dir in dirlist:
        files = os.listdir(DATADIR + dir)
        ret.append(dict(path=DATADIR + dir, files = files))
    return ret


def make_person_content(info):
    from template import TEngine   
    ret = ""
    for item in info:
        parser = DataParser(item['path'] + "/profile.txt")
        person_info = parser.parse()
        context = dict(name=person_info['name'],gender=person_info['gender'], photo=get_random_person_img(item, person_info))
        engine = TEngine("person.html", context, False) 
        engine.parse()
        html = engine.content
        ret += html

    return ret


def parse_list_to_html(rlist):
    ret = ""

    for item in rlist:
        ret += item 

    return ret

def get_random_person_img(item, info):
    plist = []
    for file in item['files']:
        if file[-3:] in IMGTYPE:
            plist.append(file)

    rd = int(random.random() * 100) % len(plist) 
    img = plist[rd]
    url = WEBDIR + "data/students/" + info['username'][0] + "/" + img 
    return url
