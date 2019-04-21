from flask.views import MethodView
from flask import render_template,redirect,url_for,request,flash
from .forms import RegisterForm, LoginForm
from ..models import User, Role
from ..email import send_email
from app import db
from flask_login import login_user,login_required,current_user,logout_user
from . import auth


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.blueprint != 'auth' \
        and request.blueprint != "main" \
        and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirm'))


class Login(MethodView):
    def __init__(self, *args, **kwargs):
        self.form = LoginForm()
        super(Login, self).__init__(*args, **kwargs)

    def get(self):
        return render_template("auth/login.html",form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            name = self.form.name.data
            password = self.form.password.data
            u = User.query.filter_by(name=name).first()
            if u is not None and u.verify_password(password):
                login_user(u,self.form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                    return redirect(next)


        flash("Invilid username or password")
        return redirect(url_for('auth.login'))




class Register(MethodView):
    def __init__(self,*args, **kwargs):
        self.form = RegisterForm()
        super(Register, self).__init__(*args,**kwargs)

    def get(self):
        return render_template("auth/register.html", form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            name = self.form.name.data
            password = self.form.password.data
            email = self.form.email.data
            u = User(name=name,password=password,email=email)
            token=u.generate_confirmation_token()
            send_email(to=email, subject="Confirm your email",template="mail/confirm", user=u, token=token)
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('auth.login'))
        return redirect(url_for('auth.register'))


class Confirm(MethodView):
    @login_required
    def get(self,token):
        if current_user.confirmed:
            return redirect(url_for("main.index"))
        if current_user.confirm(token):
            db.session.commit()
            return render_template("auth/confirmed.html")
        else:
            flash("token expires")
            return redirect(url_for('auth.unconfirm'))



class Unconfirm(MethodView):
    @login_required
    def get(self):
        return render_template("auth/unconfirm.html")


class ResendConfirm(MethodView):
    @login_required
    def get(self):
        token = current_user.generate_confirmation_token()
        send_email(to=current_user.email, subject="Confirm your email", template="mail/confirm", user=current_user, token=token)
        flash("You have resend email")
        return redirect(url_for('auth.unconfirm'))


class Logout(MethodView):
    @login_required
    def get(self):
        logout_user()
        return redirect(url_for('main.index'))