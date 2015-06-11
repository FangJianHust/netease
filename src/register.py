# -*- coding: utf-8 -*- 

import web

import db
import upload
from setting import render


class Register(object):
    
    def GET(self):
        return render.register(RegisterStatus.ORDINARY_REGISTER)       
    
    def POST(self):
        data = web.input()
        if data['passwd1'] != data['passwd2']:    #密码不一致
            return render.register(RegisterStatus.PASSOW_NOT_IDENTICAL)
        
        user = data['user'].encode("UTF-8")
        if db.check_user(user):    
            return render.register(RegisterStatus.USER_DUPLICATE)
        
        db.new_count(user, data['passwd1'])
        web.ctx.session.login = True
        web.ctx.session.uname = user
        
        up = upload.Upload()
        up.operate()
    
        web.ctx.session.photo = db.get_photo(user)
        
        raise web.seeother('/information')
 
class RegisterStatus(object):
    """ 传递给注册页面的状态值 """
    
    ORDINARY_REGISTER = 0            #正常状态
    PASSOW_NOT_IDENTICAL = 1    #密码不一致
    USER_DUPLICATE = 2                  #用户名已存在
    