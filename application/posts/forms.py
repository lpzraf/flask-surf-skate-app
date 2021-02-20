from flask_wtf import FlaskForm
from wtforms import StringField, validators


class PostForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    post_body = StringField('Blog Post Body', [validators.DataRequired()])


class DeleteForm(FlaskForm):
    pass
