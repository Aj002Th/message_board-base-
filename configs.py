#!/usr/bin/env python
#  config.py

SECRET_KEY = '123456'
# SESSION_COOKIE_SAMESITE = "None"  # 注意是字符串的None
# SESSION_COOKIE_SECURE = True

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'my_first_sql'
USERNAME = 'root'
PASSWORD = ''

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
