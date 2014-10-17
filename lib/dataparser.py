#!/usr/bin/env python
# -*- coding:utf-8 -*-  

import re

RE_PROFILE_KEY = r".*:$"
PATTERN = re.compile(RE_PROFILE_KEY)

class DataParser(object):

    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        try:
            with open(self.filename) as data:
                content = data.read()

        except IOError as e:
            print "open file error , please check"
            exit(0)

        else:
            self.content  = content
            return self.__parse_data()


    def __parse_data(self):
        if self.content is not None:
            temp = self.content.replace("\t", "").split("\n")
            profile_dict = dict()
            key = ""
            for item in temp:
                mat = re.match(PATTERN, item)
                if mat is not None:
                    key = mat.group()[:-1]
                    profile_dict[key] = []
                else:
                    profile_dict[key].append(item)
            return profile_dict


    def __shift(self, nlist):
        ret = nlist[0]
        rlist = nlist[1:]
        return ret, rlist
