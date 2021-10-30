from main import application, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    db.create_all()