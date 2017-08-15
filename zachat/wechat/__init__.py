#!/bin/env python
# -*- coding:UTF8

import wxpy
import os
file_dir = os.path.basename(__file__)
qr_dir = os.path.join(file_dir, "../static/wechat/")
def wechat_init(event=None):
    wxpy.bot = wxpy.Bot(cache_path=True,qr_path=qr_dir, console_qr=-1)