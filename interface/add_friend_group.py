#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月13日

@author: wang
'''

import socket
import time
import msgserver_login


msgserver = msgserver_login.Login(555)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((msgserver[0], 8888))

def keepalive():
    while (True):
        reqs = 'POST /im/keepalive.do HTTP/1.1\r\n'
        reqs += 'Content-Length: 0\r\n\r\n'

        sock.send(reqs)
        time.sleep(30)

body = '{\r\n'
body += '"uid":555,\r\n'
body += '"termtype":1\r\n'
body += '}'

reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)

sock.send(reqs)
res = sock.recv(10000)
if (res):
    print res

body = '{"uid":555,"termtype":1,"ftypename":"我的家人"}'
msg = 'POST /im/createfriendgroup.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)



sock.send(msg)
res = sock.recv(10000)
print res
while (True):
    res = sock.recv(10000)
    if (res):
        print res