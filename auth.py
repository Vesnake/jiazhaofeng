# _*_ coding:utf-8 _*_
# @Time :2024/5/28 10:56
# @Author : zx
# @File: auth.py
# @Description:python practitioner

from flask import Blueprint,render_template
auth = Blueprint('auth', __name__)

@auth.route('/s')
def service():
    return render_template("test.html")