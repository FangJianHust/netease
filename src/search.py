# -*- coding: utf-8 -*- 

import web 

import db
from src.base import base
from setting import render

class Search(base):
    def __init__(self):
        super(Search, self).__init__()
        
    def GET(self):
        return render.search(web.ctx.session.uname, web.ctx.session.photo)
        
    def POST(self):
        data = web.input()
        user = data['user']
        if user:
            photo = db.get_photo(user)
            return render.search(user, photo)
        