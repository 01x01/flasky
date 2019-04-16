from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField('Name: ',validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired(),Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(8,16)])
    password2 = PasswordField("Enter Password Again: ", validators=[DataRequired(),Length(8,16),EqualTo('password')])
    submit = SubmitField('Submit: ')

    def validate_email(self,filed):
        u = User.query.filter_by(email=filed.data).first()
        if u is not None:
            raise ValidationError("email exists")

    def validate_name(self,filed):
        u = User.query.filter_by(name=filed.data).first()
        if u is not None:
            raise ValidationError("username exists")


class LoginForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ",validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Submit")
