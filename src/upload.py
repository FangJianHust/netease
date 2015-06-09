# -*- coding: utf-8 -*- 

import os

import web

import db
from src.base import base
from setting import upload_dir, render

class Upload(base):
    def __init__(self):
        super(Upload, self).__init__()
    
    def GET(self):
        return render.upload()

    def POST(self):
        self.operate()
        raise web.seeother('/information')
    
    def operate(self):
        """读取头像并保存，同时更新数据库"""
        
        data = web.input(photo = {})
        filename = data['photo'].filename
        if filename:
            suffix = os.path.splitext(filename)[1]    #后缀 
            new_photo_name = web.ctx.session.uname + suffix
            (_, ext) = os.path.splitext(filename)
            filename = u'static/%s/%s' % (upload_dir, new_photo_name.decode('UTF-8'))
            with open(filename, 'wb') as fout:
                fout.write(data['photo'].file.read())

            # 作为新消息插入数据库
            uname = web.ctx.session.uname
            db.update_photo(uname, filename)
            web.ctx.session.photo = filename
            