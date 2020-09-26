#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os

def child():
    print('Hello from child',os.getpid())

def parent():
        newpid = os.fork()
        if newpid == 0:
           child()
        else:
           print('Hello from parent, fork new',os.getpid(),newpid)
           newpid1 = os.fork()
           if newpid1 == 0:
               child()
           else:
               print('Hello from parent',os.getpid(),newpid1)

parent()
