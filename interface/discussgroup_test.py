#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月22日

@author: wang
'''

import httplib2
import login_test
from intinterface_11_14port comman_function, comman_parameter
import time
import msgserver_login
import socket

ip = comman_function.ip
url = ip + ":8090/im/"

http = httplib2.Http()
token = login_test.Login()
def interface_server_test(interface_name,params,headers):
    response,content=http.request(url+interface_name+'.do?token='+token,'POST',
            body = params,
            headers = headers)
    return comman_function.strip(content)
def msgserver_test(interface,bodys,uid):
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
    res = sock.recv(10000)
    body = bodys
    msg = 'POST /im/'+interface+'.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)
    sock.send(msg)
    res = sock.recv(10000)
    return comman_function.strip(res)
    body = '{"uid":'+str(uid)+',"termtype":1}'
    msg = 'POST /im/logout.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)
    sock.send(msg)
#     while (True):
#         res = sock.recv(10000)
#         if (res):
#             print res
    


def create_discuss_group():
    return interface_server_test("creatediscgrp", '{"dgname":"hello","creatorID":510,"memberID":[510,520,530,540],"dgheadurl":"None","dgIntro":"None"}',comman_parameter.headers  )
print create_discuss_group()
def get_discuss_group_info():
    return interface_server_test("getdiscgrpinfo", '{"dgID":264}',comman_parameter.headers  )
# print get_discuss_group_info()
def get_group_member():
    return interface_server_test("getgrpmem", '{"grpID":264,"grpflag":1}', comman_parameter.headers)
# print get_group_member()
def get_joined_group():
    return interface_server_test("getjoinedgrp", '{"uid":510}', comman_parameter.headers)
# print get_joined_group()
def get_group_history_message():
    return interface_server_test("getgrphistorymsg", '{"uid":510,"grpID":264,"grpflag":1,"msgid":0,"count":10}', comman_parameter.headers)
# print get_group_history_message()
def find_discuss_group():
    return interface_server_test("finddiscgrp", '{"searchstr":"test","index":0,"count":10}', comman_parameter.headers)
# print find_discuss_group()

#未实现
# def get_invite_discuss_group():
#     return interface_server_test("getinviteDiscgrp", '{"uid":520}', comman_parameter.headers)
# print get_invite_discuss_group()

#Invalid request 不可用的请求 未实现
# def invite_join_group():
#     return msgserver_test("invitejoingrp", '{"grpID":295,"grpflag":1,"uid":520,"comment":"hello"}', 510)
# print invite_join_group()


def apply_join_group():
    return msgserver_test("applyjoingrp", '{"uid":540,"username":"test540","grpflag":1,"grpID":467,"grpname":"test","creatorID":510,"headurl":"none","mail":"none","mobile":12345678,"comment":"none"}', 540)
# print apply_join_group()
#返回{ "cmd":10000, "code":10008, "message":"Invalid request" }
def reply_group_apply():#
    return msgserver_test("replygrpapply", '{"uid":540,"grpflag":1,"grpID":264,"grpname":"test","agree":1}', 540)
# print reply_group_apply()
def set_group_info():
    return msgserver_test("setgrpinfo", '{"grpID":489,"grpflag":1,"grpname":"test","grpIntro":"aaaa","grpiconurl":"none","open":1}', 530)
# print set_group_info()
#返回{ "cmd":10000, "code":10008, "message":"Invalid request" }
# def set_group_manager():
#     return msgserver_test("setgrpmanager", '{"grpID":295,"grpflag":1,"managerID":520,"flag":1}', 510)
# print set_group_manager()

def delete_group_member():
    return msgserver_test("remgrpmem", '{"uid":520,"grpflag":1,"grpID":305,"grpname":"test","comment":"hello"}', 540)

def quit_group():
    return msgserver_test("quitgrp", '{"grpID":264,"grpflag":1,"grpname":"test","comment":"The world is  so big and I want to have a look!"}', 511)
# def delete_discuss_group():
#     return msgserver_test("deletediscgrp", '{"dgID":284}', 550)
# print delete_discuss_group()

def send_group_message():
    return msgserver_test("sendgrpmsg", '{"grpID":288,"grpflag":1,"msg":"hellokity","cookie":1437618614,"username":"test510"}', 510)

def add_group_member():
    return msgserver_test("addgrpmem", '{"grpID":494,"grpflag":1,"memberID":550,"username":"test550"}', 510)
# print add_group_member()



