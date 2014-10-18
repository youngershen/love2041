#!/usr/bin/python
# -*- coding:utf-8 -*-  

import os
import random

from config import DATADIR
from config import HTML_HEADER
from config import WEBDIR
from config import IMGTYPE
from config import PAGESIZE
from dataparser import DataParser
from request import Request

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
        ret.append(dict(username=dir,path=DATADIR + dir, files = files))
    return ret


def make_person_content(info, page = 1, page_count = 1):
    from template import TEngine
    start = int(PAGESIZE) * (int(page)  - 1) + 1 
    page_info = info[start:start+PAGESIZE]
    ret = ""
    for item in page_info:
        parser = DataParser(item['path'] + "/profile.txt")
        person_info = parser.parse()
        context = person_info
        context['username'] = person_info['username']
        context['server_addr'] = WEBDIR
        context['now_page']    = page
        context['up_page']     = [str(int(page) - 1)]
        context['down_page']   = [str(int(page) + 1)]
        context['pagecount']   = page_count
        context['photo']=get_random_person_img(item, person_info)
        #context = dict(username=person_info['username'],server_addr=WEBDIR,name=person_info['name'],gender=person_info['gender'], photo=get_random_person_img(item, person_info))
        engine = TEngine("person_sub.html", context, False) 
        engine.parse()
        html = engine.content
        ret += html

    return ret


def parse_list_to_html(rlist):
    ret = ""

    for item in rlist:
        ret +=  item 

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


def get_full_data():
    info = make_walk_data_list()
    for i in info:
        pinfo = DataParser(i['path'] + "/profile.txt").parse()
        i.update(pinfo)
        #i['profile'] = pinfo
        i['images']  = get_person_images(i['files'])
        i['server_addr'] = WEBDIR
        i['photo'] = get_random_person_img(i, pinfo)
        linfo = open(i['path'] + '/preferences.txt').read()
        i['preferences'] = linfo

    return info


def get_person_images(flist):
    ret = []
    for f in flist:
        if f[-3:] in IMGTYPE:
            ret.append(f)

    return ret

def query_userinfo(username):
    info = get_full_data()
    for i in info:
        if username == i['username'][0]:
            return i

    return None

def check_login():
    request = Request()
    data = get_full_data()
    cookies = request.get_cookie()
    username = cookies.get("username", None)
    password = cookies.get("password", None)
    
    if username is not None and password is not None:
        for person in data:
            if person['username'][0] == username and person['password'][0] == password:
                return True
            else:
                return False
    else:
        return False

def do_login(username, password):
    data = get_full_data()
    if username is not None and password is not None:
        for person in data:
            if person['username'][0] ==  username and person['password'][0] ==password:
                return True
            else:
                return False

    else:
        return False

def search_by_name(name):
    data = get_full_data()
    search_result = []
    for person in data:
        if person['name'][0] == name:
            search_result.append(person)

    return search_result

def search_person_content(result, page, page_count):
    from template import TEngine
    ret = ""
    for item in result:
        context = dict()
        context.update(item)
        context['server_addr'] = WEBDIR
        context['now_page']    = page
        context['up_page']     = [str(int(page) - 1)]
        context['down_page']   = [str(int(page) + 1)]
        context['pagecount']   = page_count
        engine = TEngine("person_sub.html", context, False) 
        engine.parse()
        html = engine.content
        ret += html
    return ret
