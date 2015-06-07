# -*- coding: utf-8 -*- 

import os

import web

from setting import render

class Register(object):
    
    def GET(self):
        return render.register()
    
    def POST(self):
        data = web.input()
        data['user']
        if data['passwd1'] != data['passwd2']:
            pass
        myfile = web.input(photo={})
        filename = myfile['photo'].filename
        suffix = os.path.splitext(filename)[1]
        web.debug(suffix)
        myfile['photo'].value 
        myfile['photo'].file.read() 
        raise ValueError
 
    