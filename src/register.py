# -*- coding: utf-8 -*- 

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
        
        user = data['user'].encode("UTF-8")
        db.new_count(user, data['passwd1'])
        web.ctx.session.login = True
        web.ctx.session.uname = user
        
        up = upload.Upload()
        up.operate()
    
        web.ctx.session.photo = db.get_photo(user)
        
        raise web.seeother('/information')
 
    