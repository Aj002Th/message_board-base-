# session.py

from flask import Blueprint, request, session
from utils import HttpError
from models import Message_board

session_bp = Blueprint("session", __name__, url_prefix="/session")


@session_bp.route('', methods=['POST'])  # 登录
def login():
    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")

    # if username is None and password is None:
    #     raise HttpError(400, "缺少参数 username\t缺少参数 password")
    # if username is None:
    #     raise HttpError(401, "缺少参数 username")
    # if password is None:
    #     raise HttpError(401, "缺少参数 password")

    record = Message_board.query.filter(Message_board.username == username).first()

    if record.username is None:
        raise HttpError(401, "不存在")
    if record.username is None:
        raise HttpError(401, "username不存在")
    if record.password != password:
        raise HttpError(401, "password不正确")

    session["user_id"] = record.id
    session["username"] = username

    return "登录成功"
