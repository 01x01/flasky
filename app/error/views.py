from flask import render_template
from . import error

# app_errorhandler 和 errorhandler的区别
# app_errorhandler 会在全局生效
# errorhandler 只会在当前蓝图生效


@error.app_errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"),404


@error.app_errorhandler(500)
def internal_error(e):
    return render_template("error/500.html"),500