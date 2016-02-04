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
    body += '"termtype":1\r\n'
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

#创建直播接口 。。。。。。。。。。。。。。正常
def create_live():
    return interface_server_test("create_live_telecast", '{"uid":550,"name":"test550","title":"professor","introduce":"null","live_name":"test_now","live_desc":"gogo","thumbnail":"None","start_time":20150818,"category":"nothing","department":"nothing","public":0,"invitees":[560,570,11,5017,5027,5038]}',comman_parameter.headers) 
# print "1\n"
# print create_live()
#获取直播频道信息接口 。。。。。。。。正常
def get_live_channel_info():
    return  interface_server_get_live_channel_info_get("get_channel_info", '{"index":0,"sort_type":1,"staus":1}', "", "", 755)
# print "2\n"
# print get_live_channel_info()
#接收直播频道上下线通知
#url 参数错误
def get_live_channel_status():
    return interface_server_test_get("interface_name", '{"channel":"my_channel","status":0}')
# print "3\n"
# print get_live_channel_status()
#获取流服务信息 正常
def get_stream_info():
    return interface_server_test_get("get_streamer_info", "areaID=1",comman_parameter.headers)
# print get_stream_info()
# print "4\n"
# print get_stream_info()
#各模块组件更新接口 
#正常
def get_modules_upgrade_info():
    return live_test_get("get_modules_upgrade_info",{"type":0,"version":"1.7.1"} )
# print "5\n"
# print get_modules_upgrade_info()
#获取流媒体服务器状态信息
#正常
def get_streamer_status():
    return interface_server_test("get_streamer_stat",'{"ip":192.168.1.11}', comman_parameter.headers)
# print get_streamer_status()
# print "6\n"
# print get_streamer_status()
#采集GSLB状态信息
#正常
def gslb_status():
    return live_test_post("gslbstat",{'version':'2.0','concurrency':65535,'areaID':1, 'uptime':123,'machineroom':'guangzhou','streamips':['192.168.1.11','192.168.1.211']}, comman_parameter.headers)
# print "7\n"
# print gslb_status()
#客户端获取GSLB状态信息
#正常
def get_gslb_status():
#     return interface_server_test('get_gslb_stat', '{"ip":"192.168.1.1"}', comman_parameter.headers)
    return live_test_post('get_gslb_stat', {"ip":"192.168.1.1"}, comman_parameter.headers)
# print "8\n"
# print get_gslb_status()

#获取GSLB地址
def get_gslb_address():
    return interface_server_test_get("get_gslb", {'areaID':1}, comman_parameter.headers)
# print get_gslb_address()



#.通知被邀请人加入直播组 
#正常
def notice_join_live():
    return msgserver_test("noticejoinlive", '{"grpID":1244,"livename":"test_now","speaker":"test550","invitees":[{"id":5017,"name":"user5017"}]}', 550)
# print notice_join_live()

#添加直播组成员
#推送不成功
def add_live_member():
    return msgserver_test("addlivemem",  '{"grpID":1165,"livename":"test_live_now","speakerID":550,"speaker":"test550","public":0,"invitees":[{"id":580,"name":"user580"}]}', 580)
# print "10\n"
# print add_live_member()

#设置直播信息
#正常，推送也ok
def update_live_info():
    return msgserver_test("updateliveinfo", '{"liveID":1244,"public":0,"livename":"morain","introduce":"i do know ","live_desc":"my_live","category":"nothing","department":"nothing","start_time":20150817,"channel":"balabalabala_test"}', 550)
# print "11\n"
# print update_live_info()

#更新直播状态
#正常,推送也ok
def update_live_status():
    return msgserver_test("updatelivestatus", '{"liveID":1244,"status":1,"public":0}', 550)
# print "12\n"
# print update_live_status()

#发送直播组消息
#推送成功（42无推送）
def send_live_message():
    return msgserver_test("sendlivemsg", '{"liveID":1164,"msg":"hello world!!!","cookie":15014946421,"public":0,"username":"test580"}', 550)
# print "13\n"
# print send_live_message()

#删除直播
#正常，无推送(42推送正常)
def delete_live():
    return msgserver_test("deletelive", '{"liveID":1165,"public":0}', 550)
# print "14\n"
# print delete_live()

#退出直播
#正常，无推送（42无推送）
def quite_live():
    return msgserver_test("quitlive", '{"liveID":1165,"public":0}', 580)
# print "18\n"
# print quite_live()








































