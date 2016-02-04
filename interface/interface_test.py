#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''
Created on 2015年7月7日

@author: wang
'''
import httplib2
import login_test
from interface import comman_function, comman_parameter

http = httplib2.Http()
token = login_test.Login()
def interface_server_test(interface_name,params,headers):
    response,content=http.request('http://120.26.126.42:8090/im/'+interface_name+'.do?token='+token,'POST',
            body = params,
            headers = headers)
    return comman_function.strip(content)


#4.2查找用户 ok
def find_user():
    return interface_server_test("finduser", '{"searchstr":"test58","index":0,"count":5}',comman_parameter.headers)
def find_user_noContype():
    return interface_server_test("finduser", '{"searchstr":"test58","index":0,"count":5}', None)
def find_user_index_010():
    return  interface_server_test("finduser", '{"searchstr":"test58","index":-10,"count":5}', comman_parameter.headers)
def find_user_count_01():
    return  interface_server_test("finduser", '{"searchstr":"test58","index":0,"count":-1}', comman_parameter.headers)
def find_user_id_20000():
    return  interface_server_test("finduser", '{"searchstr":"test10000","index":0,"count":10}', comman_parameter.headers)

#4.3 获取用户信息 ok
def get_user_info():
    return interface_server_test("getuserinfo",'{"uid":550,"detail":1}',comman_parameter.headers)
def get_user_info_noContype():
    return interface_server_test("getuserinfo", '{"uid":585,"detail":1}', None)
def find_user_info_noUid20000():
    return interface_server_test("getuserinfo", '{"uid":20000,"detail":1}', comman_parameter.headers)
def get_user_info_detail0():
    return interface_server_test("getuserinfo", '{"uid":585,"detail":0}', comman_parameter.headers)
def get_user_info_nodetail():
    return interface_server_test("getuserinfo", '{"uid":585}', comman_parameter.headers)
def get_user_info_detail010():
    return  interface_server_test("getuserinfo", '{"uid":585,"detail":-10}', comman_parameter.headers)
def get_user_info_detail10():
    return  interface_server_test("getuserinfo", '{"uid":585,"detail":10}', comman_parameter.headers)
def get_user_info_detail_5038():
    return  interface_server_test("getuserinfo", '{"uid":5038,"detail":1}', comman_parameter.headers)

#4.6获取好友列表 ok
def get_friend_list_comman():
    return interface_server_test("getfriendlist",'{"uid":585}',comman_parameter.headers)
#4.8获取好友分组 ok
def get_friend_group():
    return interface_server_test("getfritypelist", '{"uid":585}',comman_parameter.headers)

#4.14获取区域列表
def get_area():
    return  interface_server_test("getarealist", '{}',comman_parameter.headers)
#4.15获取添加好友申请
def get_add_friend_req():
    return interface_server_test("getaddfriendreq", '{"uid":586}',comman_parameter.headers)


#4.17获取最近联系人列表
def get_reccon_list():
    return interface_server_test("getrecconlist", '{"uid":585,"index":0,"count":1}',comman_parameter.headers)
#4.18获取好友历史聊天记录
def get_history_msg():
    return interface_server_test("gethistoryprimsg",'{"uid":585,"fuid":5027,"msgid":5,"count":3}',comman_parameter.headers)
#4.19设置用户信息
def set_user_info():
    return interface_server_test("setuserinfo", '{"uid":510,"username":"test585","email":"9asfas8989@qq.com","validate":0}',comman_parameter.headers)
# print set_user_info()
#4.20用户注册.
def user_register():
    return  interface_server_test("register", '{"username":"null","password":"8959069F47F28C7518374A6748487F0","email":"","mobile":"13570234203","area":231,"company":"222","department":"333","title":"444","realname":"lizhao","key":"947671","termtype":1}',comman_parameter.headers)
# print user_register()
#4.21文件上传校验
def file_upload_test():
    print "11",interface_server_test("fileuploadtest", '{"md5":"8959069F47F28C76518374A6748487F0"}',comman_parameter.headers)
#4.22文件上传
def file_upload():
    print "12",interface_server_test("fileupload", '{"uid":585}',comman_parameter.headers)
#4.45获取个人名片
def get_user_card():
    return interface_server_test("getuserbusscard", '{"uid":586,"suid":5027\n}', comman_parameter.headers)
print get_user_card()
#4.46设置个人名片
def set_user_card():
    return interface_server_test("setuserbusscard", '{"uid":585,"realname": "real_name_test585","email":"swwy_test585@swwy.com","shareemail":1,"mobile":"123456","sharemobile":0,"company":"swwy","department":"swwy","title":"professor","introduce":"\r\r\r34556\r\r\r\r\rdfg\rsdf\rdsf","donebest":"many\rsdf\rsdf\rsdf\r","education":"[]","monograph":"[]"}',comman_parameter.headers)
# print set_user_card()
#4.51获取添加好友通过验证与否信息
def get_add_friend_reply():
    return interface_server_test("getfrireply", '{"uid":585}',comman_parameter.headers)

#4.52用户存在验证
def validate_user():
    return interface_server_test("validateuser", '{"account":"test585"}',comman_parameter.headers)


