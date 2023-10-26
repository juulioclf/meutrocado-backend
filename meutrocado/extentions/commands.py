import click
from meutrocado.extentions.database import db
from meutrocado.models import User

def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()

def populate_db():
    """Populate db with sample data"""
    data = [
        User(
            username="julio.teste", password="123teste", email="julio.teste@gmail.com"
        ),
        User(
            username="julio.cesar", password="123teste", email="julio.cesar@gmail.com"
        ),
        User(
            username="julio.hehe", password="123teste", email="julio.hehe@gmail.com"
        ),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

