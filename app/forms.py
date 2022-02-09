from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SignUpForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=3, max=12)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    password1 = PasswordField('password', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('password_2', validators=[DataRequired()])
    