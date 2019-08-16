#!/usr/bin/python
#coding:gb2312

import socket
import sys

HOST=''
PORT=4433
BUFSIZ=1024
tcpSerSock=socket.socket()
tcpSerSock.bind((HOST,PORT))
tcpSerSock.listen(5)
while True:
	cs,address = tcpSerSock.accept()
	print 'got connected from',address
	recvData=cs.recv(BUFSIZ)
	print recvData
	sendData='Operating ing---'
	print sendData
	cs.send(sendData)
	#sys.exit(1)
