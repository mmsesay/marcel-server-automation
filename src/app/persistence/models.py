from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON


# enable SQLAlchemy
db = SQLAlchemy()


class InstagramModel(db.Model):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(128))


class KickofflabsModel(db.Model):
    id = db.Column(db.String, primary_key=True)
    emails = db.Column(JSON)

