#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月27日

@author: wang
'''

import httplib2
import login_test
import time
import msgserver_login
import socket
import comman_function

# http = httplib2.Http()
# token = login_test.Login()
# def interface_server_test(interface_name,params,headers):
#     response,content=http.request('http://192.168.1.14:8090/im/'+interface_name+'.do?token='+token,'POST',
#             body = params,
#             headers = headers)
#     return comman_function.strip(content)
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

def push_send_message():
    data = msgserver_test("sendmsg",'{"uid":585,"termtype":1,"fuid":587,"content":"/c[1]hello","cookie":1}', 587)
    return data[39:]

def push_add_friend_certificate_comman():
    data =  msgserver_test("addfriendreq",  '{"uid":585,"username":"test","headurl":"","fuid":586,"ftid":9,"verification":"我是fisher","fnote":"test_586" }', 586)
    return data[39:]

#确认消息是否已读   返回值不对,对功能测试即可，确认的是之前的未读消息
# def push_notice_friend_has_read_msg():
#     return msgserver_test("notifyreadmsg", '{"uid":585,"fuid":586,"termtype":1}', 585)
# #print push_notice_friend_has_read_msg()

def push_send_group_message():
    return msgserver_test("sendgrpmsg", '{"grpID":311,"grpflag":1,"msg":"nonono","cookie":1437618614,"username":"test530"}', 530)
def push_reply_add_friend_req():
    return msgserver_test("replyaddfriendreq", '{"status":1,"uid":586,"username":"test586", "headurl":"http://headurl://test586","fuid":585,"ftid":1,"fnote":"test585","reason":"","acceptorFtid":1,"acceptorFnote":"test586"}',585)


def push_add_friend_nocertificate_comman():
    data =  msgserver_test("addfriend",  '{"uid":585,"username":"test585","headurl":"test585@swwy.com","fuid":586,"ftid":1,"fnote":"test_586" }', 585)
    return data[40:]


def push_change_status():
    return msgserver_test("changeonlinestatus", '{"uid":585,"termtype":2,"status":6}', 585)


def push_create_friend_group_comman():
    data = msgserver_test("createfriendgroup",'{"uid":520,"termtype":2,"ftypename":"'+comman_function.random_str(8)+'"}', 585)
    return data[39:]

def push_delete_friend_group_comman():
    data = msgserver_test("delfriendgroup", '{"uid":585,"termtype":2,"ftid":586}', 585)
    return data[39:]

def push_rename_friend_group_comman():
    data = msgserver_test("renamefriendgroup",'{"uid":585,"termtype":2,"ftid":586,"ftypename":"'+comman_function.random_str(8)+'"}', 585)
    return data[39:]


def push_move_friend():
    data = msgserver_test("movefriend",'{"uid":585,"termtype":2,"fuid":587,"oftid":1,"nftid":2}', 585)
    return data[39:]

def push_apply_join_group():
    return msgserver_test("applyjoingrp", '{"uid":540,"username":"test540","uid":540,"headurl":"","grpflag":1,"grpID":264,"grpname":"test","creatorID":510}', 510)

def push_reply_group_apply():
    return msgserver_test("replygrpapply", '{"uid":540,"grpflag":1,"grpID":264,"grpname":"test_test","agree":1}', 540)


def push_set_group_info():
    return msgserver_test("setgrpinfo", '{"grpID":312,"grpflag":1,"grpname":"848","grpIntro":"44","open":1}', 530)

def push_delete_group_member():
    return msgserver_test("remgrpmem", '{"uid":540,"grpflag":1,"grpID":311,"grpname":"888","comment":"hello"}', 510)

# print push_delete_group_member()
def push_quit_group():
    return msgserver_test("quitgrp", '{"grpID":311,"grpflag":1,"grpname":"888","comment":"The world is  so big and I want to have a look!"}', 580)

def add_group_member():
    return msgserver_test("addgrpmem", '{"grpID":311,"grpflag":1,"memberID":550,"username":"test540"}', 510)
print add_group_member()





















    