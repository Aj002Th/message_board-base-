#!/usr/bin/env python
# app.py
from flask import Flask, jsonify, request, session
from flask_cors import *
from utils import HttpError
import configs
from exit import db
# from extentions import db
from users import users_bp
from article import article_bp
from session import session_bp
from models import Message_board
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(configs)  # 加载配置文件db.init_app(app)
# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
CORS(app, resources=r'/*', supports_credentials=True)  # 跨域
db.init_app(app)  # 绑定数据库


#  错误处理
@app.errorhandler(HttpError)
def handle_error(error):
    response = jsonify(error.show_error())
    response.status_code = error.status_code
    return response


'''
# 中间件
@app.before_request
def before():
    pass


@app.after_request
def after():
    pass
'''

# 注册蓝图
app.register_blueprint(users_bp)
app.register_blueprint(session_bp)
app.register_blueprint(article_bp)

# 程序运行
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
