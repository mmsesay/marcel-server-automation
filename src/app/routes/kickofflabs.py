"""
Filename        :   kickofflabs.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

from flask import (jsonify, Blueprint)
from ..platforms.kickofflabs import fetch_kickofflabs_users

kickofflabs = Blueprint('kickofflabs', __name__, url_prefix='/api/v1/kickofflabs')


@kickofflabs.route("/users", methods=['GET'])
def get_kickofflabs_users():
    """
    This route invoke the fetch_kickofflabs_users and returns the list of user that subscribe for
    the token give away.

    Returns:
    followers_list: The list of followers.
    """
    response = fetch_kickofflabs_users()

    return jsonify({
        "data": response,
        "status": 200
    })
