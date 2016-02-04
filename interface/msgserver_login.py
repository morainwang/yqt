#!/usr/bin/python
# vim: set fileencoding=utf-8 :

'''
Created on 2015年6月25日

@author: wang
'''
import json
import requests
import comman_function

# url = "http://192.168.1.14:8090/im/login.do/"
url = "http://120.26.126.42:8090/im/login.do/"
ifloginok = True
global token
def Login(uid):
    
    payload = {'account': "test"+str(uid),
              'password': 'e10adc3949ba59abbe56e057f20f883e',
              'termtype': 1,
              'status': 0}
     
    headers = {'Accept': 'application/json',
              'Content-Type': ' application/json;charset=UTF-8'
              }

#     session = requests.session()
#     p = session.post(url, data=json.dumps(payload), headers=headers)  
#     print 'headers', p.headers
#     print 'cookies', requests.utils.dict_from_cookiejar(session.cookies)
#     print 'html',  p.text
    
    res = requests.post(url, data=json.dumps(payload), headers=headers)  
    b = json.loads(res.text)
    ip = b["msgserver"]
    token = b["token"]
    msgserver = [ip,token]
    return msgserver

