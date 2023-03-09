from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class UserCreationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    name = StringField('Name', validators= [DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

class WorkoutsearchForm(FlaskForm):
    time = StringField('time', validators = [DataRequired()])
    muscle= StringField('muscle', validators = [DataRequired()])
    location =StringField('location', validators = [DataRequired()])
    equipment = StringField('equipment', validators = [DataRequired()])
    submit = SubmitField()
    
    


class SaveWorkout(FlaskForm):
    
    save_workout = SubmitField()