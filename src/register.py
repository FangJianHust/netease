# -*- coding: utf-8 -*- 

import web

import db
import upload
from setting import render


class Register(object):
    """ 用户注册 """
    
    def GET(self):
        return render.register(("False"," "))       
    
    def POST(self):
        data = web.input()
        
        if data['user'] =="":
            return render.register(("True", "用户名不能为空"))
        
        if len(data['user']) < 2 or len(data['user']) > 16:
            return render.register(("True", "用户名长度必须在2～16个字符之间"))
        
        if data['passwd1'] == "" or data['passwd2'] == "":
            return render.register(("True", "密码不能为空"))
        
        if data['passwd1'] != data['passwd2']:    #密码不一致
            return render.register(("True", "两次密码不一致，请重新输入！！"))
        
        if len(data['passwd1']) < 6 or len(data['passwd1']) > 20:
            return render.register(("True", "密码长度必须在6～20个字符之间"))
        
        user = data['user'].encode("UTF-8")
        if db.check_user(user):    
            return render.register(("True","用户名已经存在，请重新输入！！"))
        
        db.new_count(user, data['passwd1'])
        web.ctx.session.login = True
        web.ctx.session.uname = user
        
        up = upload.Upload()
        up.operate()
    
        web.ctx.session.photo = db.get_photo(user)
        
        raise web.seeother('/information')
    