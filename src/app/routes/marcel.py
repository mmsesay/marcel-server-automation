"""
Filename        :   marcel.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""
import time
from flask import (jsonify, request, make_response, Blueprint)
from ..platforms.marcel import MarcelServer

marcel = Blueprint('twitter', __name__, url_prefix='/api/v1/marcel')


@marcel.route("/login", methods=['GET'])
def access_marcel_server():
    """
    Invokes the marcel server class
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    marcel_server = MarcelServer()
    marcel_server.login()

    return jsonify({
            "status": 200,
            "message": "login was successfully"
        })
