"""
Filename        :   kickofflabs.py
Description     :   This file has a method that returns the kickoff emails
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

import csv


def fetch_kickofflabs_users():
    """
    This method reads the users from the file, iterate over it, get the data and return the list.

    Parameters: None
    a (int): The first number.
    b (int): The second number.

    Returns:
    followers_list: The list of followers.
    """

    # Opening JSON file
    with open('src/app/data/kickofflabs_users.csv') as users_file:
        csvreader = csv.DictReader(users_file)

        users_list = []
        for row in csvreader:
            # user_id = uuid.uuid4()
            email = row["Email"]

            users_list.append(email)

    return users_list
