#!/usr/bin/python
# vim: set fileencoding=utf-8 :

'''
Created on 2015年6月25日

@author: wang
'''
import json
import requests

 
url = 'http://192.168.1.14:8090/im/login.do'

###############正常登陆
def login_common():
    user = 585
    global rep_status
    rep_status = True
    termtype = 1
    while (termtype<=4):
        status = 0
        while (status<=6):
            payload = {'account': "test"+str(user),
                     'password': 'e10adc3949ba59abbe56e057f20f883e',
                     'termtype': termtype,
                     'status': status}
            
            headers = {'Accept': 'application/json',
                     'Content-Type': ' application/json;charset=UTF-8',
                     }
            res = requests.post(url, data=json.dumps(payload), headers=headers) 
            if "SUCCESS" not in res.text:
                rep_status = False
            else:
                pass
            status = status+1
        termtype = termtype+1
    return rep_status
# print login_common()
def login_function(payload,headers):
    res = requests.post(url, data=json.dumps(payload), headers=headers)  
    return res.text
############删除content_type
def login_ConType_error():
    return login_function({
            'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 1,
             'status': 0}, {'Accept': 'application/json'
             })
# print login_ConType_error()
############termtype值异常   

def login_Termtype_0_error():
    return login_function({'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 0,
             'status': 0}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_Termtype_0_error()
def login_Termtype_5_error():
    return login_function({'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 5,
             'status': 0}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_Termtype_5_error()
############status值异常        
def login_status_01_error():
    return login_function({'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 1,
             'status': -1}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_status_01_error()
def login_status_7_error():
    return login_function({'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 1,
             'status': 7}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_status_7_error()  
##############用户名密码错误
def login_username_error():
    return login_function({'account': "test"+str(5027),
             'password': 'e10adc3949ba59abbe56e057f20f883e',
             'termtype': 1,
             'status': 0}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_username_error()    
def login_pwd_error():
    return login_function({'account': "test"+str(585),
             'password': 'e10adc3949ba59abbe56e057f',
             'termtype': 1,
             'status': 0}, {'Accept': 'application/json',
               'Content-Type': ' application/json;charset=UTF-8'
             })
# print login_pwd_error()

