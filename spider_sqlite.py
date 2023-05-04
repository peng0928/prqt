# -*- coding: utf-8 -*-
# @Date    : 2023-04-27 13:31
# @Author  : chenxuepeng
import sqlite3
from pymysql.converters import escape_string

conn = sqlite3.connect("spider.db", timeout=10, check_same_thread=False)


def test():
    try:
        sql = '''select * from "main"."qt_spider" limit 1'''
        conn.execute(sql)
    except:
        sql = """
        CREATE TABLE "qt_spider" (
      "id" INTEGER NOT NULL,
      "url" TEXT,
      "code" text,
      "req_headers" TEXT,
      "res_headers" TEXT,
      "res_len" TEXT,
      "res_text" TEXT,
      "date" TEXT DEFAULT CURRENT_TIMESTAMP,
      "task" TEXT,
      PRIMARY KEY ("id")
    );"""
        conn.execute(sql)
        conn.commit()


def get_data():
    sql = '''select * from "main"."qt_spider" '''
    fall = conn.execute(sql).fetchall()
    return fall


def del_data():
    sql = '''DELETE from "main"."qt_spider" '''
    fall = conn.execute(sql).fetchall()
    return fall


def get_one_data(ids):
    sql = '''select * from "main"."qt_spider" where id = ?'''
    fall = conn.execute(sql, (ids,)).fetchall()
    return fall


test()
