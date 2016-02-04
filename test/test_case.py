#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''
Created on 2015年7月6日

@author: wang
'''
from function import test_case


def execute_test(workbook_name):
    print "                                                                                                          ****************"
    print "\n"
    print "                                                                                                           "+workbook_name
    print "\n"
    print "                                                                                                          ****************"
    if workbook_name == "interface_server":
        interface_server(workbook_name)
    elif workbook_name == "message_server":
        message_server(workbook_name)
    elif workbook_name == "live_message_server":
        live_message_server(workbook_name)
    elif workbook_name == "live_background_server":
        live_background_server(workbook_name)
    elif workbook_name == "discuss_group":
        discuss_group(workbook_name)
   
#接口服务器       
#接口数12      
def interface_server(workbook_name):    
    test_case(workbook_name,"find_user")
    test_case(workbook_name, "get_user_info")
    test_case(workbook_name, "get_friend_list")
    test_case(workbook_name, "get_friend_type_list")
    test_case(workbook_name, "get_add_friend_req")
    test_case(workbook_name, "get_recent_connect_list")
    test_case(workbook_name, "get_history_message")
    test_case(workbook_name, "set_user_info")
    test_case(workbook_name, "new_user_register") 
    print "未完成"
    test_case(workbook_name, "get_user_busscard")
    test_case(workbook_name, "get_friend_reply")
    test_case(workbook_name, "validate_user")
    test_case(workbook_name, "get_area_list")  
    
    
#消息服务器
#接口数11
def message_server(workbook_name):
    test_case(workbook_name, "add_friend_reqly_certificate")
    test_case(workbook_name, "add_friend_nocertificate")
    test_case(workbook_name, "delete_friend")
    test_case(workbook_name, "create_friend_group")
    test_case(workbook_name, "delete_friend_group")
    test_case(workbook_name, "rename_friend_group")
    test_case(workbook_name, "move_friend")
    test_case(workbook_name, "send_message")
    test_case(workbook_name, "reply_add_friend_req")
    test_case(workbook_name, "notice_friend_has_read_msg")
    test_case(workbook_name, "change_online_status")

#讨论组
#接口数13
def discuss_group(workbook_name):
    test_case(workbook_name, "create_discuss_group")
    test_case(workbook_name, "get_discuss_group_info")
    test_case(workbook_name, "get_group_member")
    test_case(workbook_name, "get_joined_group")
    test_case(workbook_name, "get_group_history_message")
    test_case(workbook_name, "find_discuss_group")
    test_case(workbook_name, "apply_join_group")
    test_case(workbook_name,"reply_group_apply")
    test_case(workbook_name, "set_group_info")
    test_case(workbook_name, "delete_group_member")
    test_case(workbook_name, "quit_group")
    test_case(workbook_name, "send_group_message")
    test_case(workbook_name, "add_group_member")
    
#直播消息服务器
#接口数7
def live_message_server(workbook_name):
    test_case(workbook_name,"notice_join_live")
    test_case(workbook_name,"add_live_member")
    test_case(workbook_name,"update_live_info")
    test_case(workbook_name,"update_live_status")
    test_case(workbook_name,"send_live_message")
    test_case(workbook_name,"delete_live")
    test_case(workbook_name,"quite_live")

#直播后台服务器
#接口数8
def live_background_server(workbook_name):
    test_case(workbook_name,"create_live")
    test_case(workbook_name,"get_live_channel_info")#目前获取直播频道信息的url是liveID=512
    test_case(workbook_name,"get_live_channel_status")
    test_case(workbook_name,"get_stream_info")
    test_case(workbook_name,"get_modules_upgrade_info")
    test_case(workbook_name,"get_streamer_status")
    test_case(workbook_name,"gslb_status")
    test_case(workbook_name,"get_gslb_status")





















