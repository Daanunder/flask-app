This is a basic flask app.

On development-start enter the following command in your shell:


## MAIN SETUP ##

# Python3 or higher needed
# Virtual environment is called flask and is included in project under flask-dir

# Install dependencies

sudo pip install -r requirements.txt


# Activate Virtual environment

sudo source ./flask/bin/activate


# Start app run.py to open on: http://127.0.0.1:5000/  OR  http://localhost:5000
# First make it executable, then tell python to run the script

sudo chmod a+x run.py
sudo python run.py


## DATABASE USE ##

# We will use SQLAlchemy a python Object Relational Mapper (ORM)
# As a wrapper we will use the Flask-SQLAlchemy extension
# To make updates and migrations easy SQLAlchemy-migrate is used

#Configure Database

sudo chmod a+x db_create.py
sudo python db_create.py

#Database migrations







Sufficient comments are provided.
Otherwise check this tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world