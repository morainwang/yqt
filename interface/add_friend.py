#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月13日
 
@author: wang
'''
from multiprocessing import Process
import socket
import time
import msgserver_login
from multiprocessing import Process, freeze_support
     
# if __name__ == '__main__':
#     freeze_support()
#     p = Process(target=keepalive)
#     p.start()  
#  
# 
# 
# import multiprocessing
# import time
# 
# def worker(interval):
#     while(True):
#         print("work start:{0}".format(time.ctime()))
#         time.sleep(interval)
#         print("work end:{0}".format(time.ctime()))
#         time.sleep(interval)

if __name__ == "__main__":
    
    print "end!"
    msgserver = msgserver_login.Login(510)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((msgserver[0], 8888))
    def keepalive():
        while (True):
            reqs = 'POST /im/keepalive.do HTTP/1.1\r\n'
            reqs += 'Content-Length: 0\r\n\r\n'
            print "aaa"
            sock.send(reqs)
            
            time.sleep(3)
    body = '{\r\n'
    body += '"uid":510,\r\n'
    body += '"termtype":1\r\n'
    body += '}'
     
    reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
    reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)
     
    sock.send(reqs)
    res = sock.recv(10000)
    if (res):
        print res

    p = Process(target = keepalive)
    p.start()
    while (True):
        res = sock.recv(10000)
        if (res):
            print "aa"
            print res


  
if __name__ == '__main__':
    freeze_support()
    p = Process(target=keepalive)
    p.start()  




