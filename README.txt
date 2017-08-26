This is a basic flask app.

On development-start enter the following command in your shell:


## MAIN SETUP ##

Python3 or higher needed
Virtual environment is called flask and is included in project under flask-dir

Install dependencies

$ pip install -r requirements.txt


Activate Virtual environment

$ source ./flask/bin/activate

Start app run.py to open on: http://127.0.0.1:5000/  OR  http://localhost:5000
First make it executable, then tell python to run the script

$ chmod a+x run.py
$ python run.py


## DATABASE USE ##

Create Database
============
We will use SQLAlchemy a python Object Relational Mapper (ORM)
As a wrapper we will use the Flask-SQLAlchemy extension
Create database with following command:

$ python db_create.py

Initiate migration repo
============
Flask-migrate is used for this. Initiate migration with the following command:

$ python migrate_manager.py db init         #add migration support
$ python migrate_manager.py db migrate      #add latest models to db


Other use:

$ python migrate_manager.py db migrate           ##for migration after a change in model
$ python migrate_manager.py db upgrade           ## upgrade to recently added migrations
$ python migrate_manager.py db downgrade         ## downgrade to previous
For help:

$ python migrate_manager.py db --help





Sufficient comments are provided.
Otherwise check this tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world