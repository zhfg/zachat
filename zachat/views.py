#!/bin/env python
#-*- coding:utf8
from pyramid.view import view_config
#import wxpy
#from .wechat import wechat_init
from wechatpy.enterprise import WeChatClient

corpID = 'ww9e59693956e2dd80'
secret = 'cja--4iMIZI0IvzVr-uXWsJLZEKllzrBCpKMmF-srTw'
department = 'Zabbixtest'
agentID = '1000002'

#curl 127.0.0.1:6543/send/zabbix微信报警测试/测试消息
@view_config(route_name='home', renderer='json')
def my_view(request):
    return {'bot': 'bot'}

@view_config(route_name='send',  renderer='json')
def send_message(request):
    we_err = 0
    we_msg = ''
    group = request.params.get('group')
    msg = request.params.get('message')
    client = WeChatClient(corpID, secret)
    departments = client.department.get()
    departmentID = ''
    for department in departments:
        if department['name']==group:
            departmentID = department['id']
    if departmentID == '':
        return {'code': '40001', 'msg': 'Invalid group name'}
    try:
        #print(departmentID)
        users = client.department.get_users(departmentID)
    except Exception as e:
        return {'code': '40002', 'msg': e.message}

    user_list = ''
    #user_list = '|'.join user for user in users
    for user in users:
        #print(user)
        user_list = "%s%s%s" % (user_list, user['userid'], '|')
    client.message.send_text(agentID, user_list, msg, party_ids='', tag_ids='', safe=0)
  
    return {'code': '20000', 'msg': 'sent', 'user_list': user_list}