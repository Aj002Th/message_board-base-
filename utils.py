# utils.py
# coding=gbk
from flask import session


class HttpError(Exception):
    def __init__(self, status, message):
        self.status_code = status
        self.message = message

    def show_error(self):
        return {
            "status_code": self.status_code,
            "message": self.message
        }


def if_login():
    if session.get("user_id") is None:
        raise HttpError(401, "用户未登录")
