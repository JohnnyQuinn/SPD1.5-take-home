from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    """ Form for user login """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class SignUpForm(FlaskForm):
    """ Form for user account sign up """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')