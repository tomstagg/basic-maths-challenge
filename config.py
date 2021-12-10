import json


def load_config(user):
    with open('setup.json') as json_file:
        user_setup = json.load(json_file)[user]

    return user_setup
