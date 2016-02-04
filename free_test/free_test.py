#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''
Created on 2015年7月7日

@author: wang
'''
import httplib2
import login_test
from interface_11_14 import comman_function, comman_parameter
import socket
import time
import msgserver_login
import comman_function
import json
import requests

token = login_test.Login()
http = httplib2.Http()
def interface_server_test_live(interface_name,params,headers):
    response,content=http.request('http://120.26.126.42:8090/daemon/'+interface_name+'.do?','POST',
            body = params,
            headers = headers)
    return comman_function.strip(content)
def interface_server_test_get(interface_name,params):
    url="http://120.26.126.42:8090/daemon/"+interface_name+'.do?token='+token,
    r = requests.get(url, params=params)
    return (r.text)
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


def interface_server_test(interface_name,params,headers):
    response,content=http.request('http://120.26.126.42:8090/im/'+interface_name+'.do?token='+token,'POST',
            body = params,
            headers = headers)
    print token
    return comman_function.strip(content)

# print interface_server_test("getarealist", '{}', comman_parameter.headers)
# print interface_server_test("finduser", '{"searchstr":"test58","index":0,"count":5}',comman_parameter.headers)
# print interface_server_test("getuserinfo",'{"uid":550,"detail":1}',comman_parameter.headers)
# print interface_server_test("getfriendlist",'{"uid":585}',comman_parameter.headers)
# print interface_server_test_live("create_live_telecast", '{"uid":550,"name":"test550","title":"professor","introduce":"null","live_name":"test_live_now","live_desc":"gogo","thumbnail":"None","start_time":20150818,"category":"nothing","department":"nothing","public":0,"invitees":[560,570,11,5017,5027,5038]}',comman_parameter.headers)
# print interface_server_test_get("get_streamer_info", "areaID=1")
print interface_server_test("setuserinfo", '{"uid":585,"username":"test585","email":"98989@qq.com","validate":0}',comman_parameter.headers)