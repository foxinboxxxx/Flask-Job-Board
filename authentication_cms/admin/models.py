from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# TASK(02)
from werkzeug.security import check_password_hash

db = SQLAlchemy()

## Models
class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    type = db.relationship('Type', backref=db.backref('Content', lazy=True))
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(100), nullable=False)
#!

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    # TASK(01)
    password = db.Column(db.String(100), nullable=False)
    # TASK(02)
    def check_password(self, value):
        return check_password_hash(self.password, value)
    # TASK(03) flask db init
    # TASK(03) flask db migrate
    # TASK(03) flask db upgrade
    # TASK(03) flask add-content
