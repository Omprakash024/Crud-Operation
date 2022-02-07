from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import Email,EqualTo,Length,DataRequired,ValidationError
from app.auth.models import UserCredential

def email_exists(form,field):
    email = UserCredential.query.filter_by(user_email = field.data).first()
    if email:
        raise ValidationError("Email is Alredy Exists.")


class Registration(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),Length(3,10 , message="Enter name between 3 to 10")])
    email = StringField('E-mail', validators=[DataRequired(), Email(),email_exists])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('c_password',message="password must be match.")])
    c_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')




class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('Login')

