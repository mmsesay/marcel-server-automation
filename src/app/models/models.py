from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# enable SQLAlchemy
db = SQLAlchemy()


class InstagramModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    link = db.Column(db.String(128))
    photo = db.Column(db.String(128))
