#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年8月4日

@author: wang

'''
import datetime
from random import Random
import httplib2
from test import interface_login
import xlrd
import requests
import socket
import msgserver_login
import time
import json
import os



#创建指定文件夹
def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
#         print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
#         print path+' 目录已存在'
        return False

#将产生的随机数写入到文件
def write_random_str(random_str):
    write = open("d:\\yqt_test_result\\random_str.txt","w")
    write.write(random_str)
    
#错误用例写入文件
def write_file(interface_name,result,expect):
    now = int(time.time()) 
    timeArray = time.localtime(now)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) 
    now_time = str(now_time) + "\n"
    now_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    path = ("d:\\yqt_test_result\\")+now_date
    mkdir_path=path.encode('gb18030') 
    mkdir(mkdir_path)
    file_url = mkdir_path + "\\" + str(now_date)+".txt"
    output = open(file_url, 'a+')
    line1 = "*"*100
    line2 = "\n"*3
    line3 = "The interface:" + interface_name  + "\n"
    line4 = "The real result is :" + result + "\n"
    line5 = "What we  expect is :"+ expect +"\n"*3
    line6 = "*"*100
    output.write(line1 )
    output.write(line2 )
    output.write(str(now_time))
    output.write(line3)
    output.write(line4)
    output.write(line5)
    output.write(line6 )
    output.close()
#     print "*"*30
#     print "\n"
#     print u"接口：" + interface_name  + "\n"
#     print u"返回结果为："+result+"\n"
#     print u"与预期结果："+expect+u"不符\n"
#     print "*"*30
    
    

j = 0
#发送http请求    
http = httplib2.Http()      
 
def live_test_post(interface_name,params,headers):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do"
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do"
    requests_body = dict(eval(params.encode("utf-8")))
    headers = dict(eval(headers.encode("utf-8")))
    request_json=json.dumps(requests_body)
    r=requests.post(url,data=request_json,headers=headers)
    print params
    print r.url
    return (r.text)

def live_test_get(interface_name,param):
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do"
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do"
    payload = dict(eval(param.encode("utf-8")))
    r = requests.get(url, params=payload)
    print param
    print r.url
    return (r.text)

# token = interface_login.Login()
def interface_server_test(interface_name,params,headers):
#                     response,content=http.request('http://192.168.1.14:8090/im/'+interface_name+'.do?token='+token,'POST',
                    response,content=http.request('http://120.26.126.42:8090/im/'+interface_name+'.do?token='+token,'POST',
                            body = params,
                            headers = headers)
                    print params
                    return strip(content)     
                        
def interface_server_get_live_channel_info_get(interface_name,params):
    url = "liveID=1"
#     url="http://192.168.1.11:8090/daemon/"+interface_name+".do?"+url
    url="http://120.26.126.42:8090/daemon/"+interface_name+".do?"+url
    print(url+"\n")
    r = requests.get(url, params=params)
    print params
    return (r.text)
def live_interface_server_test(interface_name,params,headers):
#     response,content=http.request('http://192.168.1.11:8090/daemon/'+interface_name+'.do?','POST',
    response,content=http.request('http://120.26.126.42:8090/daemon/'+interface_name+'.do?','POST',
            body = params,
            headers = headers)
    print params
    return strip(content)

def msgserver_test(interface,bodys,uid):
    msgserver = msgserver_login.Login(int(uid))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print msgserver[0]
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
    return strip(res)
    body = '{"uid":'+str(uid)+',"termtype":1}'
    msg = 'POST /im/logout.do?token={:s} HTTP/1.1\r\nContent-Length: {:d}\r\n\r\n{:s}'.format(msgserver[1], len(body), body)
    sock.send(msg)
    
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

#去掉读取字符串的换行符
def strip(line):
        line = line.strip("\n")
        return line

   
#读取excel表内的参数
def test_case(workbook_name,sheet_name):
    global failed_count 
    failed_count =0
    bk = xlrd.open_workbook(workbook_name+".xls") # 打开excel文件
    sh = bk.sheet_by_name(sheet_name)# 打开excel表
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print "\n"
    print "                                                                                                           "+sheet_name
    print "\n"
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    nrows = sh.nrows # 获取总行数
    for i in range(1,nrows):  
        print "==================================================================================================================================================================="
        print i
        global j 
        j = j+1
        print j
        type = sh.cell_value(i,0)
        interface_name = sh.cell_value(i,1)
        method = sh.cell_value(i,2)
        param=sh.cell_value(i,3)
        header = sh.cell_value(i,4)
        uid = sh.cell_value(i,5)
        expect = sh.cell_value(i,6)
        expect = expect.encode("utf-8")
        error = sh.cell_value(i,7)
        print int(uid)
        global token
        token = interface_login.Login(int(uid))
        if type == "interface_server":
            if method == "GET":
                pass
            elif method == "POST":
                header=dict(eval(header.encode("utf-8")))
                result = interface_server_test(interface_name, param, header)
                print result
                print expect
                if result == expect:
                    print "ok"
                else:
                    print "error"
                    write_file(interface_name, result, expect)
                

        elif type == "message_server":
            if method == "GET":
                pass
            elif method == "POST":
                pass
            elif method == "SOCKET":
                if interface_name == "createfriendgroup" or interface_name =="renamefriendgroup":
                    param = param +'"' + random_str(8) +'"}'
                print param
                result = msgserver_test(interface_name, param, int(uid))
                print result
                print expect
                if result == expect:
                    print "ok"
                else:
                    print "error"
                    write_file(interface_name, result, expect)

        elif type == "discuss_group":
            if method == "GET":
                pass
            elif method == "POST":
                header=dict(eval(header.encode("utf-8")))
                print interface_server_test(interface_name, param, header)

            elif method == "SOCKET":
                print param
                print msgserver_test(interface_name, param, int(uid))
        elif type =="live_message_server":
            if method == "GET":
                pass
            elif method =="POST":
                pass
            elif method == "SOCKET":
                print msgserver_test(interface_name, param, int(uid))

        elif type =="live_background_server":
            if method == "POST(interface)":
                header=dict(eval(header.encode("utf-8")))
                print live_interface_server_test(interface_name, param, header)

            elif method == "GET(interface)":
                if interface_name == "get_channel_info":#                     url_str =[550,"",""]#                     url_str = [560,1,""]#                     url_str =["","",""
                    url_str = ["","",1]
                    print interface_server_get_live_channel_info_get(interface_name, param)

            elif method == "POST(live)":
                print live_test_post(interface_name, param, header)

            elif method == "GET(live)":
                print live_test_get(interface_name, param)

                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        