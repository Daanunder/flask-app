# init script for app package [app package = app folder]

#flask import
from flask import Flask

#app variable /w flask instance
app = Flask(__name__)
app.config.from_object('config')

#SQLAlchemy import & setup
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# import views module from flask-app package
from app import views, models


