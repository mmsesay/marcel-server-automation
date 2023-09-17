"""
Filename        :   instagram.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

from flask import (jsonify, Blueprint)
from ..platforms.instagram import fetch_instagram_followers

from ..persistence.models import db, InstagramModel

instagram = Blueprint('instagram', __name__, url_prefix='/api/v1/instagram')


@instagram.route("/followers", methods=['GET'])
def get_twitter_followers():
    """
    This route invoke the fetch_instagram_followers and returns the list of followers data.

    Returns:
    followers_list: The list of followers.
    """
    response = fetch_instagram_followers()

    obj = InstagramModel(name="test", link="test", photo="Test")
    db.session.add(obj)
    db.session.commit(obj)

    return jsonify({
        "data": response,
        "status": 200
    })
