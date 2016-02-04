#!/usr/bin/python
# vim: set fileencoding=utf-8 :
'''

@author: zhen.wang
'''


from pyExcelerator import *
from xlrd import open_workbook 
import xlrd
import xlwt
import sqlite3
from xlutils.copy import copy 
import os
import msvcrt
from xlrd import open_workbook 
import xlrd
import os
import xlwt
from trace import find_strings

result_file_name = "d:\\ab_test_result\\test.xls"
log_file_name = "C:\\Users\\wang\\Desktop\\test.log"

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
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
 
nrows = 0

# #Tuner测试的新建文件
def New_File(filename):
    mkpath_dir1=(u"d:\\ab_test_result\\").encode('gb18030') 
    mkdir(mkpath_dir1)
    if os.path.exists(filename) == False:
#新建一个excel文件
        file = xlwt.Workbook() #注意这里的Workbook首字母是大写
        #新建一个sheet
        table = file.add_sheet(u'test_result')
        table.write(0,0,u"接口名")
        table.write(0,1,u"并发数")
        table.write(0,2,u"网络类型")
        table.write(0,3,u"请求数")
        table.write(0,4,u"总耗时")
        table.write(0,5,u"请求失败数")
        table.write(0,6,u"Total transferred")
        table.write(0,7,u"Total POSTed")
        table.write(0,8,u"Time per request/level")
        table.write(0,9,u"Time per request")
        table.write(0,10,u"Requests per second")
        table.write(0,11,u"Transfer rate total")
        table.write(0,12,u"longest request")
        #写入数据table.write(行,列,value)
        file.save(filename)
    else:
        pass

def Write_Excel_12(col,tmp_string,):  
    global nrows     
    rb = xlrd.open_workbook(result_file_name,formatting_info = True)     
    sh = rb.sheet_by_name(u"test_result")   
    nrows = sh.nrows 
    ncols = sh.ncols
    wb = copy(rb)
    ws = wb.get_sheet(0)
    ws.write(nrows,col,tmp_string)
    os.remove(result_file_name)
    wb.save(result_file_name)
    
def Write_Excel(col,tmp_string,):  
    global nrows     
    rb = xlrd.open_workbook(result_file_name,formatting_info = True)     
    sh = rb.sheet_by_name(u"test_result")   
    nrows = sh.nrows -1
    ncols = sh.ncols
    wb = copy(rb)
    ws = wb.get_sheet(0)
    ws.write(nrows,col,tmp_string)
    os.remove(result_file_name)
    wb.save(result_file_name)    

def write_str_12(col,find_str):
    file_object = open(log_file_name)
    try:
        all_the_text = file_object.read( )
        count = int(all_the_text.find(find_str))
        longest_request =  all_the_text[count-8:count]
        Write_Excel_12(col,longest_request)
    finally:
        file_object.close( )

def write_str(col,find_str):
    file_object = open(log_file_name)
    try:
        all_the_text = file_object.read( )
        count = int(all_the_text.find(find_str))
        longest_request =  all_the_text[count-8:count]
        Write_Excel(col,longest_request)
    finally:
        file_object.close( )

 
New_File(result_file_name)         
write_str_12(12, "(longest request)")
write_str(11, "kb/s total")
write_str(10, "[#/sec] (mean)")
write_str(9, "[ms] (mean, across all concurrent requests)")
write_str(8, "[ms] (mean)")
write_str(7, "HTML transferred:")
write_str(6, "bytes\nTotal POSTed:")
#write_str(5, "HTML transferred:")
write_str(4, "seconds")
write_str(3, "Failed requests:")
write_str(2, "Server Port: ")
write_str(1, "Time taken for tests:")
write_str(0, ".do/\nDocument Length:")


















    
