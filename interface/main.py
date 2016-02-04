#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月13日
 
@author: wang
'''

import unittest
import login
impimport interface_11_14rom intinterface_11_14port comman_assert
from intinterface_11_14port comman_reply
import msgserver_test
from intinterface_11_14gout import logout
from intinterface_11_14mman_reply import get_friend_group_str

find_user = interface_test.find_user()
find_user_id_20000 = interface_test.find_user_id_20000()
get_user_info = interface_test.get_user_info()
get_user_info_detail0 = interface_test.get_user_info_detail0()
get_user_info_detail010 = interface_test.get_user_info_detail010()
get_user_info_detail10 = interface_test.get_user_info_detail10()
get_user_info_nodetail = interface_test.get_user_info_nodetail()
find_user_info_noUid20000 = interface_test.find_user_info_noUid20000()
add_friend_certificate_comman = msgserver_test.add_friend_certificate_comman()
add_friend_certificate_ftid4 = msgserver_test.add_friend_certificate_ftid4()
add_friend_nocertificate_comman =msgserver_test.add_friend_nocertificate_comman()
add_friend_nocertificate_ftid4 = msgserver_test.add_friend_nocertificate_ftid4()
get_friend_list_comman = interface_test.get_friend_list_comman()
get_friend_group = interface_test.get_friend_group()
delete_friend = msgserver_test.delete_friend_comman()
get_user_info_noContype = interface_test.get_user_info_noContype()
find_user_count_01 = interface_test.find_user_count_01()
#测试用例集Login
class test_Login(unittest.TestCase):
       
    def test_login_comman(self):
        self.assertEqual(login.login_common(),True , comman_assert.login_failed_str)
    def test_login_ConType_error(self):
        self.assertIn("Invalid content type", login.login_ConType_error(), comman_assert.login_failed_str)
    def test_login_Termtype_0_error(self):
        self.assertIn("Lack or wrong body parameters", login.login_Termtype_0_error(), comman_assert.login_failed_str)
    def test_login_Termtype_5_error(self):
        self.assertIn("Lack or wrong body parameters", login.login_Termtype_5_error(), comman_assert.login_failed_str)
    def test_login_status_01_error(self):
        self.assertIn("Lack or wrong body parameters", login.login_status_01_error(), comman_assert.login_failed_str)         
    def test_login_status_7_error(self):
        self.assertIn("Lack or wrong body parameters", login.login_status_7_error(), comman_assert.login_failed_str)
    def test_login_username_error(self):
        self.assertIn("No user or password wrong", login.login_username_error(), comman_assert.login_failed_str)
    def test_login_pwd_error(self):
        self.assertIn("No user or password wrong", login.login_pwd_error(), comman_assert.login_failed_str)
           
          
#测试用例集查找用户
class test_find_user(unittest.TestCase):
  
    def test_find_user_comman(self):
        self.assertEqual(comman_reply.find_user_data,find_user, comman_assert.find_user_failed_str)
    def test_find_user_noContype(self):
        self.assertIn(comman_reply.no_conType_str, interface_test.find_user_noContype(), comman_assert.find_user_failed_str)
    def test_find_user_index10(self):
        self.assertIn(comman_reply.wrong_parameters_str, interface_test.find_user_index_010(), comman_assert.find_user_failed_str)
    def test_find_user_count01(self):
        self.assertIn(comman_reply.wrong_parameters_str,interface_test.find_user_count_01(), comman_assert.find_user_failed_str)
    def test_find_user_nodata20000(self):
        self.assertIn(comman_reply.no_data_str,find_user_id_20000, comman_assert.find_user_failed_str)
 
 
#测试用例集获取用户信息
class test_get_user_info(unittest.TestCase):
      
    def test_get_user_info_comman(self):
        self.assertEqual(comman_reply.get_user_info_data, get_user_info, comman_assert.get_user_info_failed_str)
    def test_find_user_info_noContype(self):
        self.assertIn(comman_reply.no_conType_str, get_user_info_noContype, comman_assert.get_user_info_failed_str) 
    def test_find_user_info_noUid20000(self):
        self.assertIn(comman_reply.no_data_str, find_user_info_noUid20000, comman_assert.get_user_info_failed_str) 
    def test_get_user_info_detail0(self):
        self.assertEqual(comman_reply.find_user_info_str, get_user_info_detail0, comman_assert.get_user_info_failed_str) 
    def test_get_user_info_nodetail(self):       
        self.assertEqual(comman_reply.find_user_info_str, get_user_info_nodetail, comman_assert.get_user_info_failed_str) 
    def test_get_user_info_detail010(self):
        self.assertEqual(comman_reply.find_user_info_detail_str, get_user_info_detail010, comman_assert.get_user_info_failed_str) 
    def test_get_user_info_detail10(self):
        self.assertEqual(comman_reply.find_user_info_detail_str, get_user_info_detail10, comman_assert.get_user_info_failed_str)
   
        
#测试用例集添加好友（需要验证）
class test_add_fried_certificate(unittest.TestCase):
    
    #被添加的用户在线时
    def test_add_friend_online(self):
        self.assertEqual(comman_reply.add_friend_str, add_friend_certificate_comman, comman_assert.add_friend_nocertificate_failed_str)
        self.assertEqual(comman_reply.add_friend_str,add_friend_certificate_ftid4 , comman_assert.add_friend_nocertificate_failed_str)
    #被添加用户不在线时
    def test_add_friend_offline(self):
        logout(586)
        self.assertEqual(comman_reply.add_friend_str, add_friend_certificate_comman, comman_assert.add_friend_nocertificate_failed_str)
        self.assertEqual(comman_reply.add_friend_str,add_friend_certificate_ftid4 , comman_assert.add_friend_nocertificate_failed_str)


#测试用例集添加好友（不需验证）
class test_add_fried_nocertificate(unittest.TestCase):
    
    #被添加的用户在线时
    def test_add_friend_online(self):
        self.assertEqual(comman_reply.add_frind_nocertificate_str,add_friend_nocertificate_comman, comman_assert.add_friend_nocertificate_failed_str)
        self.assertEqual(comman_reply.add_frind_nocertificate_ftid4_str,add_friend_nocertificate_ftid4 , comman_assert.add_friend_nocertificate_failed_str)
    #被添加用户不在线时
    def test_add_friend_offline(self):
        logout(586)
        self.assertEqual(comman_reply.add_frind_nocertificate_str,add_friend_nocertificate_comman, comman_assert.add_friend_nocertificate_failed_str)
        self.assertEqual(comman_reply.add_frind_nocertificate_ftid4_str,add_friend_nocertificate_ftid4 , comman_assert.add_friend_nocertificate_failed_str)


#测试用例集 获取好友列表
class test_get_friend_list(unittest.TestCase):
    
    def test_get_frind_list(self):
        self.assertEqual(comman_reply.add_friend_comman_str, get_friend_list_comman, comman_assert.get_friend_list_failed_str)
        
        
#测试用例集 删除好友
class test_delete_friend(unittest.TestCase):
    
    def test_delete_friend(self):
        self.assertEqual(comman_reply.delete_friend_str, delete_friend, comman_assert.get_friend_list_failed_str)
        
       
#测试用例集 获取好友分组
class test_get_friend_group(unittest.TestCase):
    def test_get_friend_group(self):
        print "aa"+get_friend_group_str+"aa"
        print "aa"+get_friend_group+"aa"
        self.assertEqual(comman_reply.get_friend_group_str, get_friend_group, comman_assert.get_friend_list_failed_str)
    



if __name__ == "__main__":
    unittest.main()