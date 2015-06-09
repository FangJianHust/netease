# -*- coding: utf-8 -*- 

import web 

import db
from setting import render

class Login(object):
    
    def GET(self):
        return render.login('False')
    
    def POST(self):
        data = web.input()
        user = data['user'].encode("UTF-8")
        passwd = data['passwd']
        if db.check_account(user, passwd):
            web.ctx.session.login = True
            web.ctx.session.uname = user
            web.ctx.session.photo = db.get_photo(user)
            web.debug(web.ctx.session.photo)
            raise web.seeother('/information')
        else:
            return render.login('True')
    
class Quit(object):
    
    def GET(self):
        web.ctx.session.login = False
        web.ctx.session.uname = ''
        web.ctx.session.photo = None
        raise web.seeother('/login')
    