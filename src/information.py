# -*- coding: utf-8 -*- 

from setting import render

class Information(object):
    
    def GET(self):
        return render.information()