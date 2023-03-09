from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from secrets import token_hex


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    My_Workout = db.relationship('My_Workout', backref='author', lazy=True)

    def __init__(self, username, name, email, password, wins=0):
        self.username = username
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.token = token_hex(16)
        

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def databaseCommit():
        db.session.commit()

class Workout(db.Model):
    id = db.Column(db.String, primary_key=True)
    Time = db.Column(db.String(50), nullable=False, unique=False)
    Location = db.Column(db.String(50), nullable=False, unique=False)
    Muscle = db.Column(db.String(50), nullable=False, unique=False)
    Equipment = db.Column(db.String(50), nullable=False, unique=False)
    key = db.Column(db.String(200), nullable=False, unique=True)
    My_Workout = db.relationship('My_Workout', backref='workout', lazy=True)

    def __init__(self,id,Time, Location, Muscle, Equipment, key):
        self.Time = Time
        self.id= id
        self.Location = Location
        self.Muscle = Muscle
        self.Equipment = Equipment
        self.key = key

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def removeFromDB(self):
        db.session.delete(self)
        db.session.commit()

class My_Workout(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Workout_name = db.Column(db.String(200), db.ForeignKey('workout.key'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, user_id, Workout_name):
        self.user_id = user_id
        self.Workout_name = Workout_name

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()