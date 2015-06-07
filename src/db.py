# -*- coding: utf-8 -*- 

import web 

from setting import database

db = web.database(
                  dbn=database['engine'], 
                  db=database['db'], 
                  user=database['user'], 
                  passwd=database['123456']
                  )

def new_count(name_, passwd_):
    db.insert('account', name=name_, passwd=passwd_)