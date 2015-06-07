# -*- coding: utf-8 -*- 

import web 

database = "mysql"
debug = True

# url规则
urls = (
    '/', 'src.login.Login',
    '/login', 'src.login.Login',
    '/register', 'src.register.Register',
    '/information', 'src.information.Information',
)

render = web.template.render('templates')