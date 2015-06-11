# -*- coding: utf-8 -*- 

import web

import db
from src.base import base
from setting import *

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
            new_photo_name = new_photo_name.decode('UTF-8')
            absolute_path = u'%s%s' % (upload_dir, new_photo_name)
            with open(absolute_path, 'wb') as fout:    #文件保存到绝对路径
                fout.write(data['photo'].file.read())

            # 作为新消息插入数据库
            web.ctx.session.photo = relative_path + new_photo_name   #数据库中存放的是相对路径
            db.update_photo(web.ctx.session.uname, web.ctx.session.photo)
            
            