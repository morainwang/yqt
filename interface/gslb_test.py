#!/usr/bin/env python
# coding=utf-8
'''
Created on 2015年8月3日

@author: wang
'''
#!/usr/bin/env python
# coding=utf-8

import httplib2
import requests


http = httplib2.Http()

def interface_server_test_push():
    url="http://192.168.1.14:8095/gslb/getstreamsrcsrvaddr.do"
    r = requests.get(url)
    print r.url
    return (r.text)


def interface_server_test_get():
    url="http://192.168.1.14:8095/gslb/getstreamsrvaddr.do"
    r = requests.get(url)
    print r.url
    return (r.text)



def get_stream_push_addr():
    return interface_server_test_push()
print get_stream_push_addr()

def get_stream_srv_addr():
    return interface_server_test_get()
print get_stream_push_addr()


