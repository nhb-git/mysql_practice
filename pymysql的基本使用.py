#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/11/2020  9:25 PM 
# 文件名称   ：pymysql的基本使用.py
import pymysql


user = input('user:>> ').strip()
password = input('password:>> ').strip()

# 建立连接
conn_obj = pymysql.connect(
    host='192.168.137.131',
    port=3306,
    user='userinfo',
    password='123456',
    db='db1',
    charset='utf8'
)

# 获取游标
cursor = conn_obj.cursor()

# 执行sql语句
try:
    sql = 'select * from userinfo where user="%s" and pwd="%s"' % (user, password)
    rows = cursor.execute(sql)
finally:
    cursor.close()
    conn_obj.close()

# 判断
if rows:
    print('登录成功')
else:
    print('登录失败')
