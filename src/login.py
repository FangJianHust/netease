# -*- coding: utf-8 -*- 

import web 

from setting import render

class Login(object):
    
    def GET(self):
        return render.login()
    
    def POST(self):
        raise web.seeother("/information")
    