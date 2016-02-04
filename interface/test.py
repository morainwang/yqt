#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年7月31日

@author: wang
'''
import live_test
import comman_parameter

#1.创建直播 创建者550
#组内成员560，570
#public：0
# print interface_server_test("create_live_telecast", '{"uid":550,"name":"test550","title":"professor","introduce":"null","live_name":"test_live_now","live_desc":"gogo","start_time":20150729,"category":"nothing","department":"great","public":0,"invitees":[560,570,5017]}',comman_parameter.headers) 

#2.获取gslb地址
#"gslb":"192.168.1.14"
# print live_test.interface_server_test_get("get_gslb", {'areaID':1}, comman_parameter.headers)

#3.app获取频道信息
#获取所有的直播（没有加筛选条件）
# print live_test.interface_server_test("get_channel_info", '',comman_parameter.headers)

#4.设置频道信息。主要是设置channel
#设置频道名称为my_channel
# print live_test.msgserver_test("updateliveinfo", '{"liveID":512,"public":0,"livename":"new_name","introduce":"i do know how to introduce him!!haha","live_desc":"my_live","category":"nothing","department":"nothing","start_time":20150806,"channel":"my_channel"}', 550)

#5.通知其他成员加入（还要测试下推送，560和570都应受到推送）
#将590加入到直播组
# print live_test.msgserver_test("noticejoinlive", '{"grpID":512,"livename":"test_live_now","speaker":"test550","invitees":[{"id":590,"name":"user590"}]}', 550)

#6.获取流服地址
#192.168.1.11/channel=my_channel
#获取的时候，在浏览器内直接发请求，跳转后的URL为真实地址

#7.查询流服状态
#content":[{"Company":"SWWY","Author":"ChenZhengQiang","Date":"2015/5/12","Version":"v1.7.1","cpu_occupy":0.979364,"mem_occupy":57.697976,"net":{"received_bytes":17911,"transmited_bytes":805,"received_packets":200,"transmited_packets":6},"viewers":{"total":0},"channels":{"total":0,"set":[""]},"cameras":{"total":0,"set":[""]},"resources":{"total":0,"set":[""]}}]}
#content":[{"Company":"SWWY","Author":"ChenZhengQiang","Date":"2015/5/12","Version":"v1.7.1","cpu_occupy":0.979364,"mem_occupy":57.697976,"net":{"received_bytes":17911,"transmited_bytes":805,"received_packets":200,"transmited_packets":6},"viewers":{"total":0},"channels":{"total":0,"set":[""]},"cameras":{"total":0,"set":[""]},"resources":{"total":0,"set":[""]}}]}
# print live_test.interface_server_test("get_streamer_stat",'{"ip":192.168.1.11}', comman_parameter.headers)

#8.更新直播状态未直播开始
#（这里要推送给所有的组内成员）
# print live_test.msgserver_test("updatelivestatus", '{"liveID":512,"status":1,"public":0}', 550)

#9.camera开始推流
#用pc camera模拟推流

#10.流服受到流之后，向gslb发送频道上线通知
#gslb接收频道上线通知
# print live_test.interface_server_test_get("channel_stat", {"channel":"my_channel","status":1},comman_parameter.headers)

#11.成员申请观看直播
#首先获取收流地址，浏览器内发请求，获得跳转地址

#12.成员开始观看直播
#

#13.直播成员各种操作，发消息，退出等
#

#14.app通知camera关闭推流
#流服收流中断之后，返回下线通知

#15.#gslb接收频道下线通知
# print live_test.interface_server_test_get("channel_stat", {"channel":"my_channel","status":2},comman_parameter.headers)

#15.修改直播状态
#
# print live_test.msgserver_test("updatelivestatus", '{"liveID":512,"status":2,"public":0}', 550)
























