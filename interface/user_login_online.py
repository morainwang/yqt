#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process, freeze_support
import socket
import time
import msgserver_login


def login(uid):
    
    msgserver = msgserver_login.Login(uid)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((msgserver[0], 8888))
    
    def keepalive():
        while (True):
            reqs = 'POST /im/keepalive.do HTTP/1.1\r\n'
            reqs += 'Content-Length: 0\r\n\r\n'
    
            sock.send(reqs)
            time.sleep(30)
    
    body = '{\r\n'
    body += '"uid":'+str(uid)+',\r\n'
    body += '"termtype":1\r\n'
    body += '}'
    
    reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
    reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)
    
    sock.send(reqs)
    res = sock.recv(1000)
    if (res):
        print   res
    while (True):
        res = sock.recv(1000)
        if (res):
#             return res
            print res
          
    if __name__ == '__main__':
        freeze_support()
        p = Process(target=keepalive)
        p.start()
login(588)