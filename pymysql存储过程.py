#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/11/2020  9:52 PM 
# 文件名称   ：pymysql之增删改查.py
import pymysql


# 建立连接
conn = pymysql.connect(
    host='192.168.137.131',
    port=3306,
    user='root',
    password='123456',
    db='db2',
    charset='utf8'
)

# 获取游标
# cursor = conn.cursor()
# 基于字典的游标，可以显示字段名称
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 执行存储过程
# 调用无参数存储过程
# cursor.callproc('p1')

# 调用有参数存储过程
cursor.callproc('p2', (2, 5, 0))
print(cursor.fetchall())

# 关闭游标和连接
cursor.close()
conn.close()
