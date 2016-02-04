#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年8月20日

@author: wang
'''
from test_case import execute_test
import function
from test.function import write_random_str

# random_str = function.random_str(8)
# now_str_in_file = random_str
# write_random_str(random_str)

#51个接口
#415条用例

execute_test("interface_server")
execute_test("live_message_server")
execute_test("discuss_group")
execute_test("live_background_server")
execute_test("message_server")
# execute_test("push_message")
