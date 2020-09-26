#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os

def child():
    print('Hello from child',os.getpid())

def parent():
    for i in range(3):
        print(i)
        newpid = os.fork()
        if newpid == 0:
           child()
        else:
           print('Hello from parent',os.getpid(),newpid)

parent()
