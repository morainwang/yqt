#!/usr/bin/python
# vim: set fileencoding=utf-8 :

'''
Created on 2015年7月23日

@author: wang
'''
import json
import httplib2
import requests
from interface import comman_function, comman_parameter
import msgserver_login
import time
import socket
import login_test



token = login_test.Login()
http = httplib2.Http()
def live_test_post(interface_name,params,headers):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do?token="+token
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do?token="+token
    requests_body = params
    request_json=json.dumps(requests_body)
    r=requests.post(url,data=request_json,headers=headers)
    return (r.text)
def live_test_get(interface_name,param):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do?"+token
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do?"+token
    r = requests.get(url, params=param)
    return (r.text)


def interface_server_test(interface_name,params,headers):
#     response,content=http.request("http://192.168.1.11:8090/daemon/"+interface_name+'.do?','POST',
    response,content=http.request("http://120.26.126.42:8090/daemon/"+interface_name+'.do?','POST',
            body = params,
            headers = headers)
    return comman_function.strip(content)
def interface_server_test_get(interface_name,params):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+'.do?token='+token,
    url="http://120.26.126.42:8090/daemon/"+interface_name+'.do?token='+token,
    r = requests.get(url, params=params)
    return (r.text)

def interface_server_get_live_channel_info_get(interface_name,params,uid,invitee,liveID):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do?liveID="+str(liveID)
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do?liveID="+str(liveID)
    r = requests.get(url, params=params)
    print (r.text)
    print url    

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
    body += '"termtype":1,\r\n'
    body += '"status":0\r\n'
    body += '}'
    
    reqs = 'POST /im/login.do?token={:s} HTTP/1.1\r\n'.format(msgserver[1])
    reqs += 'Content-Length: {:d}\r\n\r\n{:s}'.format(len(body), body)
    
    sock.send(reqs)
    res = sock.recv(10000)
    print res
    body = bodys
    msg = 'POST /im/'+interface+'.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)
    sock.send(msg)
    res = sock.recv(10000)
    return comman_function.strip(res)
    body = '{"uid":'+str(uid)+',"termtype":1}'
    msg = 'POST /im/logout.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)
    sock.send(msg)

def create_live():
    return interface_server_test("create_live_telecast", '{"uid":550,"name":"test550","title":"professor","introduce":"null","live_name":"test_now","live_desc":"gogo","thumbnail":"None","start_time":20150818,"category":"nothing","department":"nothing","public":0,"invitees":[560,570,11,5017,5027,5119]}',comman_parameter.headers) 
# print "1\n"
# print create_live()

def notice_join_live():
    return msgserver_test("noticejoinlive", '{"grpID":1516,"livename":"test_now","speaker":"test550","invitees":[{"id":1,"name":"user590"}]}', 550)
# print notice_join_live()

def update_live_info():
    return msgserver_test("updateliveinfo", '{"liveID":1516,"public":0,"livename":"morain","introduce":"i do know ","live_desc":"my_live","category":"nothing","department":"nothing","start_time":20150817,"channel":"CCD29B70D511"}', 550)
# print "11\n"
# print update_live_info()

def update_live_status():
    return msgserver_test("updatelivestatus", '{"liveID":1516,"status":1,"public":0}', 550)
# print "12\n"
print update_live_status()

def delete_live():
    return msgserver_test("deletelive", '{"liveID":1516,"public":0}', 550)
# print "14\n"
# print delete_live()

def live_progress():
    create_live_res = create_live()
    create_live_res = json.loads(create_live_res)
    content = create_live_res["content"]
    print content
    content = json.loads(content)
    live_ID = content["live_ID"]
    print live_ID

# live_progress()




































