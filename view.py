# _*_ coding:utf-8 _*_
# @Time :2024/5/28 10:46
# @Author : zx
# @File: view.py
# @Description:python practitioner

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")