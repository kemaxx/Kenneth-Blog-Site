from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    name = StringField("Name",validators=[DataRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = EmailField(label="Email",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label='Login')


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comments", validators=[DataRequired()])
    submit = SubmitField(label='Submit Comment')


