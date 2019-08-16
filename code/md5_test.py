#!/usr/bin/python
#-*- coding: UTF-8 -*-
import hashlib

def get_token():
    md5str = "shan275abc"
    m1 = hashlib.md5()
    m1.update(md5str.encode("utf-8"))
    token = m1.hexdigest()
    return token

print get_token()
