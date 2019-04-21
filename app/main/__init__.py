from flask import Blueprint


# 给蓝图命名
# __name__ 方便查找template文件
# url_prefix 所有的url 均为 http://127.0.0.1:5000/index/xxxx
main = Blueprint("main",__name__)

from . import views, routes
