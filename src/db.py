# -*- coding: utf-8 -*- 

import json

import web 

from setting import db_path

f = file(db_path)
database = json.load(f)
            
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
    
def check_account(user_, passwd_):
    res = db.select('account', where='user=$user_ and passwd=$passwd_', vars=locals())
    if len(res) > 0:
        return True
    else:
        return False
    
def check_user(user_):
    res = db.select('account', where='user=$user_', vars=locals())
    if len(res) > 0:
        return True
    else:
        return False

def get_photo(user_):
    try:
        return db.select('account', where='user=$user_', vars=locals())[0].photo
    except IndexError:
        return None