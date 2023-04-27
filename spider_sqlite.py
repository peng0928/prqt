# -*- coding: utf-8 -*-
# @Date    : 2023-04-27 13:31
# @Author  : chenxuepeng
import sqlite3
from pymysql.converters import escape_string

conn = sqlite3.connect("spider.db", timeout=10, check_same_thread=False)


def get_data():
    sql = '''select * from "main"."qt_spider" '''
    fall = conn.execute(sql).fetchall()
    return fall

def get_one_data(ids):
    sql = '''select * from "main"."qt_spider" where id = ?'''
    fall = conn.execute(sql, ids).fetchall()
    return fall


if __name__ == '__main__':
    get_data()