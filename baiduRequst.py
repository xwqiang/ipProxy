#!/usr/bin/python
# -*- coding: UTF-8 -*-
import util
import threading

class baiduRequest(threading.Thread):
    count = 0
    proxy = None
    name = None
    ok = None


    def __init__(self,proxy,name):
        self.count += 1
        self.proxy = proxy
        self.name = name

    def run(self):
        self.ok = util.validUsefulProxy(self.proxy)

