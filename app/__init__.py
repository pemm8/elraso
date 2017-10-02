import os 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin

app = Flask(__name__)

# app temp config
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY='uisgiwiuh25982iwnqmfhbsgiu20j201fiofo2'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False 

app.config.from_object(__name__)

# db
db = SQLAlchemy(app)

# flask admin
admin = Admin(app, template_mode='bootstrap3')

from app import views, models