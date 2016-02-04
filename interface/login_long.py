#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月13日

@author: wang
'''
#!/usr/bin/env python
# coding=utf-8

#长连接是30秒内向服务器发链接请求，服务器的判定时间是60秒
#下面的脚本未实现长连接，只要在60秒内发请求，下面的脚本能够收到响应即可
import msgserver_login
import socket
import comman_function

ip = comman_function.ip
url = ip + ":8090/daemon/"


def login_long(uid):
    msgserver = msgserver_login.Login(uid)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((msgserver[0], 8888))
    
    body = '{\r\n'
    body += '"uid":'+str(uid)+',\r\n'
    body += '"termtype":1\r\n'
    body += '}'
     
    reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
    reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)
     
    sock.send(reqs)
    res = sock.recv(1000)   
    if res:
        print res
        file_object = open('test.txt', 'w')
        file_object.write(res)
        file_object.close( )
    while (1):
        res = sock.recv(1000)
        if (res):
            print res
            file_object = open('test.txt', 'w')
            file_object.write(res)
            file_object.close( )
        else:
            break
login_long(520)     










