#!/usr/bin/env python
# article.py

from flask import Blueprint, request, session
from utils import HttpError, if_login
from models import Message_board
from exit import db

article_bp = Blueprint("message", __name__, url_prefix="/message")


@article_bp.route('/post_message', methods=['POST'])  # 发布留言
def post_message():
    data = request.get_json(force=True)
    message = data.get("message")

    if_login()

    if message is None:
        raise HttpError(400, "缺少参数 message")

    user = Message_board.query.filter(Message_board.id == session.get("user_id")).first()
    user.message = message
    nickname = user.nickname

    db.session.commit()

    return {
        "nickname": nickname,
        "message": message
    }


@article_bp.route('/change_message', methods=['POST'])  # 修改留言
def change_message():
    data = request.get_json(force=True)
    message = data.get("message")

    if_login()

    if message is None:
        raise HttpError(400, "缺少参数 message")

    # Message_board.query.filter_by(Message_board.id == session.get("user_id")).update({'message': message})
    user = Message_board.query.filter(Message_board.id == session.get("user_id")).first()
    user.message = message
    nickname = user.nickname

    db.session.commit()

    return {
        "nickname": nickname,
        "message": message
    }


@article_bp.route('/delete_message', methods=['DELETE'])  # 删除留言
def delete_message():
    if_login()

    message = ''
    user = Message_board.query.filter(Message_board.id == session.get("user_id")).first()
    user.message = message

    db.session.commit()

    return "留言删除成功"
