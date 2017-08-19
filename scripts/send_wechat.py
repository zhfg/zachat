#!/bin/env python
#-*- coding:utf8
import urllib
import requests
import os, sys

#http://127.0.0.1:6543/?message=asdfasdf%3Basdfasdf%0Aeiasjdf%3Baksdjfa%3Bskldfj%0Aasdfeijasd%3Bfkajsdf%0Aeiajs%3Bdflkajeiaspeoifjasdfa%0Aasdfieja%3Bsdkfjas%3Bfiejaieojasdfasdf%0A&group=zabbix%E5%BE%AE%E4%BF%A1%E6%8A%A5%E8%AD%A6%E6%B5%8B%E8%AF%95

url = 'http://127.0.0.1:6543/send'
argc = len(sys.argv)
if argc < 3:
    print("Need less 2 argments, %d givened" % (argc-1))
    sys.exit(-1)

group = sys.argv[1]
message = sys.argv[2]
payload = {'group': group, 'message': message}

r = requests.get(url, params=payload)
if (r.status_code == 200):
    sys.exit(0)
else:
    sys.exit(-2)

"""
"""
