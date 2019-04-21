from flask.views import MethodView
from flask import render_template
from flask_login import current_user


class Index(MethodView):
    def get(self):
        return render_template("main/index.html",user = current_user)
