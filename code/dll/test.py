#-*- coding:utf-8 -*-
import ctypes

dll = ctypes.windll.LoadLibrary('.\XLib\Stream.dll')
dll.utils_markHttpUrl_new(0,0,'dddddfdf')