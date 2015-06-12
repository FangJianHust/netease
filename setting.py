# -*- coding: utf-8 -*- 

import os

import web 

curdir = os.path.dirname(__file__)

# 上传文件夹
relative_path = '/static/upfile/'           #相对路径存入数据库，用于浏览器访问
upload_dir = curdir + relative_path   #绝对路径用于保存上传的头像

database = {
            'engine': 'mysql',
            'db': 'netease',
            'user': 'fangjian',
            'passwd': '123456'
            }
debug = False

# url规则
urls = (
    '/', 'src.login.Login',
    '/login', 'src.login.Login',
    '/quit', 'src.login.Quit',
    '/register', 'src.register.Register',
    '/information', 'src.information.Information',
    '/upload', 'src.upload.Upload',
    '/search', 'src.search.Search',
)

render = web.template.render(curdir+'/templates/', base='base')