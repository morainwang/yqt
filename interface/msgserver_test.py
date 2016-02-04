#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月13日

@author: wang
'''

import socket
import time
import msgserver_login
import comman_function
import json


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
    
#添加好友（需验证）
def add_friend_certificate_comman():
    data =  msgserver_test("addfriendreq",  '{"uid":1000000,"username":"test","headurl":"","fuid":586,"ftid":9,"verification":"我是fisher","fnote":"test_586" }', 585)
    return data[39:]

def add_friend_certificate_ftid4():
    data = msgserver_test("addfriendreq",  '{"uid":587,"username":"test587","headurl":"test587@swwy.com","fuid":585,"ftid":1,"verification":"我是587","fnote":"test_556" }', 586)
    return data[39:]
#msgserver_test("addfriendreq",  '{"uid":587,"username":"test587","headurl":"test587@swwy.com","fuid":585,"ftid":1,"verification":"我是11","fnote":"test_556" }', 586)
#msgserver_test("addfriendreq", '{"uid":20000,"username":"test588","headurl":"test586@swwy.com","fuid":585,"ftid":4,"verification":"我是fisher","fnote":"test_556" }', 586)
#msgserver_test("addfriendreq", '{"uid":586,"username":"test586","headurl":"test586@swwy.com","fuid":20000,"ftid":4,"verification":"我是fisher","fnote":"test_556" }', 586)
#msgserver_test("addfriendreq", '{"uid":586,"username":"test586","headurl":"test586@swwy.com","fuid":585,"ftid":4,"verification":"我是fisher","fnote":"测试586" }', 586)

#添加好友（不需验证）

# def add_friend_nocertificate_comman():
#     data =  msgserver_test("addfriend",  '{"uid":585,"username":"test585","headurl":"test585@swwy.com","fuid":586,"ftid":1,"fnote":"test_586" }', 585)
#     return data[40:]

def add_friend_nocertificate_comman():
    fuid = 350
    n = 1
    while fuid <= 500:
        data =  msgserver_test("addfriend",  '{"uid":333,"username":"test333","headurl":"test585@swwy.com","fuid":'+str(fuid)+',"ftid":1,"fnote":"test_'+str(n)+'" }', 333)
        fuid = fuid + 1
        n = n+1
        print  data[40:]
add_friend_nocertificate_comman()

def add_friend_nocertificate_ftid4():
    data =  msgserver_test("addfriend",  '{"uid":585,"username":"test585","headurl":"test585@swwy.com","fuid":586,"ftid":4,"fnote":"test_586" }', 585)
    return data[40:]
# msgserver_test("addfriend", '{"uid":586,"username":"test586","headurl":"test586@swwy.com","fuid":588,"ftid":2,"fnote":"test_588" }', 586)
# msgserver_test("addfriend", '{"uid":20000,"username":"test586","headurl":"test586@swwy.com","fuid":585,"ftid":4,"fnote":"test_585" }', 586)
# msgserver_test("addfriend", '{"uid":587,"username":"test586","headurl":"test586@swwy.com","fuid":585,"ftid":4,"fnote":"test_585" }', 586)
# msgserver_test("addfriend", '{"uid":586,"username":"test586","headurl":"test586@swwy.com","fuid":20000,"ftid":4,"fnote":"test_585" }', 586)


#删除好友
def delete_friend_comman():
    data = msgserver_test("delfriend", '{"uid":585,"fuid":586}', 585)
    return data[39:]
# msgserver_test("delfriend", '{"uid":586,"fuid":585}', 586)
# msgserver_test("delfriend", '{"uid":20000,"fuid":585}', 586)
# msgserver_test("delfriend", '{"uid":586,"fuid":20000}', 586)

#创建好友分组
def create_friend_group_comman():
    data = msgserver_test("createfriendgroup",'{"uid":585,"termtype":2,"ftypename":"'+comman_function.random_str(8)+'"}', 585)
    return data[39:]

# msgserver_test("createfriendgroup",  '{"uid":585,"termtype":1,"ftypename":"'+random_str(8)+'"}', 585)
# msgserver_test("createfriendgroup",  '{"uid":585,"termtype":2,"ftypename":"'+random_str(8)+'"}', 585)
# msgserver_test("createfriendgroup",  '{"uid":585,"termtype":3,"ftypename":"'+random_str(8)+'"}', 585)
# msgserver_test("createfriendgroup",  '{"uid":585,"termtype":4,"ftypename":"'+random_str(8)+'"}', 585)


#{ "cmd":2012, "ftid":287, "ftypename":"sgETfn1r" }
#删除好友分组
def delete_friend_group_comman():
    data = msgserver_test("delfriendgroup", '{"uid":585,"termtype":3,"ftid":1}', 585)
    return data[39:]

#msgserver_test("delfriendgroup", '{"uid":585,"termtype":1,"ftid":104}', 585)
#msgserver_test("delfriendgroup", '{"uid":585,"termtype":1,"ftid":104}', 585)

#重命名好友分组
def rename_friend_group_comman():
    data = msgserver_test("renamefriendgroup",'{"uid":585,"termtype":2,"ftid":167,"ftypename":"'+comman_function.random_str(8)+'"}', 167)
    return data[39:]

# msgserver_test("renamefriendgroup",'{"uid":585,"termtype":1,"ftid":167,"ftypename":"'+random_str(8)+'"}', 585)
#  
# msgserver_test("renamefriendgroup",'{"uid":585,"termtype":1,"ftid":167,"ftypename":"'+random_str(8)+'"}', 585)


#移动好友到其他分组
def move_friend():
    data = msgserver_test("movefriend",'{"uid":587,"termtype":1,"fuid":586,"oftid":1,"nftid":1}', 585)
    return data[39:]

#发送消息
def send_message():
    data = msgserver_test("sendmsg",'{"uid":585,"termtype":1,"fuid":587,"content":"/c[1]hello","cookie":1}', 585)
    return data[39:]
#应答添加好友申请

def reply_add_friend_req():
    return msgserver_test("replyaddfriendreq", '{"status":2,"uid":586,"username":"test586", "headurl":"http://headurl://test586","fuid":585,"ftid":1,"fnote":"test585","reason":"","acceptorFtid":1,"acceptorFnote":"test586"}',586)
# print reply_add_friend_req()
def notice_friend_has_read_msg():
    return msgserver_test("notifyreadmsg", '{"uid":585,"fuid":586,"termtype":1}', 585)
# print notice_friend_has_read_msg()
#改变在线状态
def change_status():
    return msgserver_test("changeonlinestatus", '{"uid":585,"termtype":1,"status":6}', 585)



