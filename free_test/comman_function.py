#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''
Created on 2015年7月6日

@author: wang
'''
from random import Random

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