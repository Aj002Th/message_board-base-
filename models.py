#!/usr/bin/env python
# models
from exit import db


class Message_board(db.Model):  # 建表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(50), nullable=False)  # 非空  密码
    nickname = db.Column(db.String(50))  # 默认：xx  昵称
    age = db.Column(db.String(20))  # 年龄
    gender = db.Column(db.String(20))  # 男/女 性别
    address = db.Column(db.String(20))  # 住址
    message = db.Column(db.String(255))  # 留言
    post_time = db.Column(db.DateTime)  # 留言发布时间
    change_time = db.Column(db.DateTime)  # 留言修改时间
    like = db.Column(db.String(255))  # 记录谁点赞
    comment = db.Column(db.String(255))  # 评论内容
    answer = db.Column(db.String(255))  # 回复评论的内容
    color_letter = db.Column(db.String(10))  # 默认：白  留言字体颜色
    color_bubble = db.Column(db.String(10))  # 留言气泡颜色
    is_administrators = db.Column(db.Boolean)  # 默认：false  管理员权限


'''应该是不需要的
    def __init__(self, username, password):
        self.username = username
        self.password = password
'''
