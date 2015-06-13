#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import sys
import os

import web


curdir = os.path.dirname(__file__)  #获取当前的目录，用于得到文件的绝对路径
sys.path.append(curdir)
from setting import *

app = web.application(urls, globals())
web.config.debug = debug
web.config.session_parameters['cookie_name'] = 'py_pytalk_sid'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 60*60*5,
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = '3u12m8xXo0is'
web.config.session_parameters['expired_message'] = 'Session expired'
session = web.session.Session(app, web.session.DiskStore(curdir+'/data/sessions'), initializer={'login': False})

def session_hook():
    web.ctx.session = session     #即可在全局访问session
app.add_processor(web.loadhook(session_hook))
application = app.wsgifunc()    #wsgi访问的需要   


