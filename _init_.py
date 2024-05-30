# _*_ coding:utf-8 _*_
# @Time :2024/5/25 11:12
# @Author : zx
# @File: _init_.py
# @Description:python practitioner

from flask import Flask

def create_app():
    app = Flask(__name__)

    from view import views
    from auth import auth
    app.config['SECRET_KEY'] ='jiazhaofeng page'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app