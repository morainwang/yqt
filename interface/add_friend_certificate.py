#!/usr/bin/env python
# coding=utf-8
#body = '{"uid":4,"username":"test4","headurl":"test4@swwy.com","fuid":3,"ftid":1,"verification":"我是fisher","fnote":"test_3" }'
#msg = 'POST /im/addfriend.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(configs["token2"], len(body), body)


from multiprocessing import Process
import socket
import time
import msgserver_login


msgserver = msgserver_login.Login(589)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((msgserver[0], 8888))

def keepalive():
    while (True):
        reqs = 'POST /im/keepalive.do HTTP/1.1\r\n'
        reqs += 'Content-Length: 0\r\n\r\n'

        sock.send(reqs)
        time.sleep(30)

body = '{\r\n'
body += '"uid":589,\r\n'
body += '"termtype":1\r\n'
body += '}'

reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)

sock.send(reqs)
res = sock.recv(10000)
if (res):
    print res

body = '{"uid":589,"username":"test589","headurl":"test589@swwy.com","fuid":588,"ftid":1,"verification":"我是fisher","fnote":"test_556" }'
msg = 'POST /im/addfriendreq.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)



sock.send(msg)
res = sock.recv(10000)
print res

while (True):
    res = sock.recv(10000)
    if (res):
        print res
    else:pass
        


        

