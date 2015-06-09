# -*- coding: utf-8 -*- 

import web 

# 上传文件夹
upload_dir = 'upfile'

database = {
            'engine': 'mysql',
            'db': 'netease',
            'user': 'fangjian',
            'passwd': '123456'
            }
debug = True

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

render = web.template.render('templates/', base='base')