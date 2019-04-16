from flask.views import MethodView
from flask import render_template
from .forms import RegisterForm, LoginForm
from ..models import User, Role


class Login(MethodView):
    def get(self):
        self.form = LoginForm()
        return render_template("auth/login.html",form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            name = self.form.name.data
            u = User.query.filter_by(name=name).first()
            if u:
                pass


class Register(MethodView):
    def get(self):
        self.form = RegisterForm()
        return render_template("auth/register.html",form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            name = self.form.name.data
            password = self.form.password.data
            email = self.form.email.data
            u = User(name=name,password=password,email=email)


