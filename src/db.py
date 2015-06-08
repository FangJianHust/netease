# -*- coding: utf-8 -*- 

import web 

from setting import database

db = web.database(
                  dbn=database['engine'], 
                  db=database['db'], 
                  user=database['user'], 
                  passwd=database['passwd']
                  )

def new_count(user_, passwd_):
    db.insert('account', user=user_, passwd=passwd_)
    
def update_photo(user_, photo_):
    db.update('account', where='user=$user_',
                     vars=locals(),photo=photo_)