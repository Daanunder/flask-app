
#cross site request forgery (CSRF)
WTF_CSRF_ENABLED = True
SECRET_KEY = 'stupidos-are-not-smart'

#Data base config
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASK_MIGRATE_REPO = os.path.join(basedir, 'flask_migrate.db')
SQLALCHEMY_ECHO = True