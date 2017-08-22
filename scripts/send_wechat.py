#!/bin/env python
#-*- coding:utf8
import urllib
import requests
import os, sys,logging

#http://127.0.0.1:6543/?message=asdfasdf%3Basdfasdf%0Aeiasjdf%3Baksdjfa%3Bskldfj%0Aasdfeijasd%3Bfkajsdf%0Aeiajs%3Bdflkajeiaspeoifjasdfa%0Aasdfieja%3Bsdkfjas%3Bfiejaieojasdfasdf%0A&group=zabbix%E5%BE%AE%E4%BF%A1%E6%8A%A5%E8%AD%A6%E6%B5%8B%E8%AF%95

url = 'http://222.92.56.244:7788/send'
argc = len(sys.argv)
if argc < 3:
    print("Need less 2 argments, %d givened" % (argc-1))
    sys.exit(-1)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/tmp/send_wechat.log',
                filemode='a')

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
