from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class UserForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])


class DeleteForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


# follow or unfollow form
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
