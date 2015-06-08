# -*- coding: utf-8 -*- 

import os

import web

import db
import upload
from setting import render

class Register(object):
    
    def GET(self):
        return render.register('False')
    
    def POST(self):
        data = web.input()
        if data['passwd1'] != data['passwd2']:
            return render.register('True')    #密码不一致
        
        web.ctx.session.login = True
        web.ctx.session.uname = data['user'].encode("UTF-8")
        db.new_count(data['user'], data['passwd1'])
        up = upload.Upload()
        up.POST()
 
    