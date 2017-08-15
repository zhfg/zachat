#!/bin/env python
# -*- coding:UTF8

import wxpy
import os, threading
file_dir = os.path.basename(__file__)
qr_dir = os.path.join(file_dir, "../static/wechat/")
def wechat_init(event=None):
    print(event)
    thread = threading.Thread(target=wechat_login, name="wehcat_login")
    thread.start()

def wechat_login():
    wxpy.bot = wxpy.Bot(cache_path=True,qr_path=qr_dir, console_qr=-2)

    @wxpy.bot.register(msg_types=wxpy.FRIENDS)
        # 自动接受验证信息中包含 'connext' 的好友请求
    def auto_accept_friends(msg):
        # 判断好友请求中的验证文本
        if 'connext' in msg.text.lower():
            # 接受好友 (msg.card 为该请求的用户对象)
            new_friend = bot.accept_friend(msg.card)
            # 或 new_friend = msg.card.accept()
            # 向新的好友发送消息
            new_friend.send('你已是我的好友，请将我加入对应的报警群')