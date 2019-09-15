import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# login manager
login_manager = LoginManager()
# Declare the application
app = Flask(__name__)

# the base file path
basedir = os.path.dirname(__file__)

# the various configurations of the application
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db definations
db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'
