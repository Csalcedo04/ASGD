from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class RegisterForm():
    username = StringField('user', validators = [InputRequired()])
    email = StringField('email', validators = [InputRequired()])
    password = StringField('password', validators = [InputRequired(), EqualTo('confirm')])
    confirm = StringField('confirm Password', validators = [InputRequired()])