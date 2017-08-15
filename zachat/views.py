#!/bin/env python
#-*- coding:utf8
from pyramid.view import view_config
import wxpy
from .wechat import wechat_init

#curl 127.0.0.1:6543/send/zabbix微信报警测试/测试消息
@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    return {'bot': wxpy.bot}

@view_config(route_name='send', request_method='GET', renderer='templates/mytemplate.jinja2')
def send_message(request):
    we_err = 0
    we_msg = ''
    bot = wxpy.bot
    print bot.alive
    if not bot.alive:
        wechat_init()
    group = request.params.get('group')
    msg = request.params.get('message')
    try:
        my_group = bot.groups().search(group)[0]
    except Exception as e:
        logging.error("Error:", e.message)
        we_err = -2   #找不到相就的组
        we_msg = e.message
    finally:
        print(my_group)
        my_group.send(msg)
        we_err = 0
        we_msg = "OK: Sended message %s to group %s " % (group, msg)
    return {'we_err': we_err, 'we_msg': we_msg}