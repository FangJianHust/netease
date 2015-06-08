# -*- coding: utf-8 -*- 

import web 

class base(object):
    def __init__(self):
        pass
        if not self.is_login():   #任何权限操作之前，都需要判断session
            raise web.seeother('/login')
    def is_login(self):
        return hasattr(web.ctx.session, 'login') and web.ctx.session.login == True
