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
    user='userinfo',
    password='123456',
    db='db1',
    charset='utf8'
)

# 获取游标
# cursor = conn.cursor()
# 基于字典的游标，可以显示字段名称
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 执行sql
# 增、删、改
sql = 'insert into userinfo(user,pwd) values(%s,%s)'
# 单行插入
# rows = cursor.execute(sql, ('bao', '123'))

# 多行插入
rows = cursor.executemany(sql, [('xxx', '123'), ('yyy', '123'), ('zzz', '123')])
# 显示插入前的最后id的值
print(cursor.lastrowid)
conn.commit()
print(cursor.lastrowid)

# 查
# rows = cursor.execute('select * from userinfo')
# 显示一行查询结果
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# 一次取多条结果
# print(cursor.fetchmany(2))

# 一次取出所有结果
# print(cursor.fetchall())

# 游标的相对移动和绝对移动
# cursor.scroll(2, mode='absolute')
# print(cursor.fetchone())
# cursor.scroll(1, mode='relative')
# print(cursor.fetchone())

# 关闭游标和连接
cursor.close()
conn.close()
