from meutrocado.extentions.database import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    username = db.Column(db.String(140), unique=True)
    email = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(140))