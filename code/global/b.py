#!/usr/bin/python
# -*- coding: utf-8 -*-

import globalvar as gl

name = gl.get_value('name')
score = gl.get_value('score')

print("%s: %s" % (name, score))
