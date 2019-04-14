from flask.views import MethodView
from flask import render_template


class Main(MethodView):
    def get(self):
        return render_template("main/index.html")
