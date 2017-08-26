from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

#Migration setup
migrate = Migrate(app, db)

#Manager for migration commands
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()