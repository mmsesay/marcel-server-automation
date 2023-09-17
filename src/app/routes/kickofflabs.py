"""
Filename        :   kickofflabs.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""
import uuid

from flask import (jsonify, Blueprint)
from ..platforms.kickofflabs import fetch_kickofflabs_users
from ..persistence.models import db
from ..persistence.models import KickofflabsModel


kickofflabs = Blueprint('kickofflabs', __name__, url_prefix='/api/v1/kickofflabs')


@kickofflabs.route("/users", methods=['GET'])
def get_kickofflabs_users():
    """
    This route invoke the fetch_kickofflabs_users and returns the list of user that subscribe for
    the token give away.

    Returns:
    followers_list: The list of followers.
    """
    try:
        response = fetch_kickofflabs_users()

        obj = KickofflabsModel(id=uuid.uuid4(), emails={"emails": response})
        db.session.add(obj)
        db.session.commit()

        return jsonify({
            "data": response,
            "message": "All kickofflabs users",
            "status": 200
        })
    except:
        return jsonify({
            "data": response,
            "message": "Failed to fetch kickofflabs users",
            "status": 500
        })
