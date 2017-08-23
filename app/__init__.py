# init script for app package [app package = app folder]

#flask import
from flask import Flask

#app variable /w flask instance
app = Flask(__name__)

# import views module from app package
from app import views

