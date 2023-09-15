# __init__.py
"""
Filename        :   __init__.py
Description     :   This file contains the whole logic for the application
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# import the routes
from .routes.instagram import instagram
from .routes.kickofflabs import kickofflabs
from .models.models import db

# instantiate flask
app = Flask(__name__)
CORS(app)  # enable cors

# add the different blueprints
app.register_blueprint(instagram)
app.register_blueprint(kickofflabs)

# app secret key
app.config['SECRET_KEY'] = 'devkey'
app.config["JWT_SECRET_KEY"] = "testsecretkey"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://maej:maejor123@localhost:5432/scrape_db'  # sqlite:///' + os.path.join(app.root_path, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# enable flask migrate
migrate = Migrate(app, db)

# import the models
from .models import models
