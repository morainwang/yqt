#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''
Created on 2015年7月6日

@author: wang
'''
from intinterface_11_14terface_test import get_friend_group

no_conType_str = "Invalid content type"
wrong_parameters_str = "Lack or wrong body parameters"
no_data_str = "No data"
find_user_info_detail_str = '{ "cmd":3, "code":0, "message":"SUCCESS", "content": { "uid":585,"username":"test585","email":"swwy_test585@swwy.com","mobile":"123456","signature":"I am test585","headurl":"http://192.168.1.14:8090/images/874963fc37c0f693284a472be1a01a12.jpg","question":"","answer":"","validate":1 } }'
find_user_data = '{ "cmd":2, "code":0, "message":"SUCCESS", "content": [ { "uid":58,"username":"test58","company":"swwy","department":"swwy","headurl":"http://headurl://test58","question":"","answer":"","validate":1,"status":6 }, { "uid":580,"username":"test580","company":"swwy","department":"swwy","headurl":"http://headurl://test580","question":"","answer":"","validate":1,"status":6 }, { "uid":581,"username":"test581","company":"swwy","department":"swwy","headurl":"http://headurl://test581","question":"","answer":"","validate":1,"status":6 }, { "uid":582,"username":"test582","company":"swwy","department":"swwy","headurl":"http://headurl://test582","question":"","answer":"","validate":1,"status":6 }, { "uid":583,"username":"test583","company":"swwy","department":"swwy","headurl":"http://headurl://test583","question":"","answer":"","validate":1,"status":6 } ] }'
find_user_info_str = '{ "cmd":3, "code":0, "message":"SUCCESS", "content": { "uid":585,"username":"test585","headurl":"http://192.168.1.14:8090/images/874963fc37c0f693284a472be1a01a12.jpg" } }'
get_user_info_data = '{ "cmd":3, "code":0, "message":"SUCCESS", "content": { "uid":585,"username":"test585","email":"swwy_test585@swwy.com","mobile":"123456","signature":"I am test585","headurl":"http://192.168.1.14:8090/images/874963fc37c0f693284a472be1a01a12.jpg","question":"","answer":"","validate":1 } }'
add_friend_str = '{ "cmd":1001, "code":0, "message":"SUCCESS" }'
add_frind_nocertificate_str = '{ "cmd":1002, "code":0, "message":"SUCCESS", "content": { "fuid":586, "ftid":1, "fnote":"test_586", "username":"test586", "headurl":"http://headurl://test586", "signature":"I am test586" } }'
add_frind_nocertificate_ftid4_str = '{ "cmd":1002, "code":0, "message":"SUCCESS", "content": { "fuid":586, "ftid":4, "fnote":"test_586", "username":"test586", "headurl":"http://headurl://test586", "signature":"I am test586" } }'
add_friend_comman_str = '{ "cmd":5, "code":0, "message":"SUCCESS", "content": [ \n{ "ftid":1,"status":6,"fnote":"test_586","signature":"I am test586","headurl":"http://headurl://test586","fuid":586 } ] }'
get_friend_group_str = '{ "cmd":4, "code":0, "message":"SUCCESS", "content": [ { "ftid":1,"ftypename":"我的好友" }, { "ftid":2,"ftypename":"陌生人" }, { "ftid":94,"ftypename":"我的同学" } ] }'
delete_friend_str = '{ "cmd":1003, "code":0, "message":"SUCCESS", "content": { "fuid":586 } }'




