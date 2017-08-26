# init script for app package [app package = app folder]

#flask import
from flask import Flask

#Database import
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app variable /w flask instance
app = Flask(__name__)
app.config.from_object('config')

#Database initiation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import views module from app package
from app import views, models




