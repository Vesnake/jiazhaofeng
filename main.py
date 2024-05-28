# _*_ coding:utf-8 _*_
# @Time :2024/5/25 11:23
# @Author : zx
# @File: main.py
# @Description:python practitioner

from _init_ import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)