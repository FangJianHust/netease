# -*- coding: utf-8 -*- 

from src.base import base
from setting import render

class Information(base):
    def __init__(self):
        super(Information, self).__init__()
    
    def GET(self):
        return render.information()