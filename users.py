# users.py

from flask import Blueprint, request, session, jsonify
from utils import HttpError, if_login
from models import Message_board
from exit import db

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route('', methods=['POST'])  # 注册
def register():
    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")
    nickname = data.get("nickname")

    if username is None and password is None:
        raise HttpError(400, "缺少参数 username\t缺少参数 password")
    if username is None:
        raise HttpError(400, "缺少参数 username")
    if password is None:
        raise HttpError(400, "缺少参数 password")

    record = Message_board.query.filter(Message_board.username == username).first()

    if record:
        raise HttpError(400, "username已存在")

    user = Message_board(username=username, password=password, nickname=nickname)
    db.session.add(user)
    db.session.commit()

    return "注册成功"


@users_bp.route('/set_my_information', methods=['POST'])  # 设置个人的资料
def set_my_information():
    data = request.get_json(force=True)
    nickname = data.get("nickname")
    age = data.get("age")
    gender = data.get("gender")

    if_login()

    if nickname is None or age is None or gender is None:
        raise HttpError(400, "缺少必要的参数")

    '''
    Message_board.query.filter_by(Message_board.id == session.get("user_id")).update({'nickname': nickname})
    Message_board.query.filter_by(Message_board.id == session.get("user_id")).update({'age': age})
    Message_board.query.filter_by(Message_board.id == session.get("user_id")).update({'gender': gender})
    '''
    user = Message_board.query.filter(Message_board.id == session.get("user_id")).first()
    user.nickname = nickname
    user.age = age
    user.gender = gender

    db.session.commit()

    return "个人信息设置成功"


@users_bp.route('/show_my_homepage', methods=['GET'])  # 显示个人主页
def show_my_homepage():
    if_login()

    user = Message_board.query.filter(Message_board.id == session.get("user_id")).first()

    if user is None:
        raise HttpError(400, "该用户不存在")

    username = user.username
    nickname = user.nickname
    age = user.age
    gender = user.gender

    return {
        "username": username,
        "nickname": nickname,
        "age": age,
        "gender": gender
    }


@users_bp.route('/show_ones_homepage', methods=['GET'])   # 显示某个用户的个人主页
def show_ones_homepage():
    data = request.get_json(force=True)
    username = data.get("username")
    if_login()

    if username is None:
        raise HttpError(400, "缺少必要的参数")

    user = Message_board.query.filter(Message_board.username == username).first()

    if user is None:
        raise HttpError(400, "该用户不存在")

    nickname = user.nickname
    age = user.age
    gender = user.gender

    return {
        "username": username,
        "nickname": nickname,
        "age": age,
        "gender": gender
    }


@users_bp.route('/show_message', methods=['GET'])  # 显示某个用户的留言
def show_message():
    data = request.get_json(force=True)
    username = data.get("username")
    if_login()

    if username is None:
        raise HttpError(400, "缺少必要的参数")

    user = Message_board.query.filter(Message_board.username == username).first()

    if user is None:
        raise HttpError(400, "该用户不存在")

    message = user.message

    return {
        "message": message
    }


@users_bp.route('/show_all_message', methods=['GET'])  # 获取所有用户的留言
def show_all_message():
    all_users = Message_board.query.all()
    all_information = []
    for x in all_users:
        all_information.append([x.username, x.nickname, x.message])
    all_information_after = jsonify(all_information)
    return all_information_after
