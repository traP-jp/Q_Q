from traq.api.user_api import UserApi
from .traq_api import client

userapi = UserApi(client)


def get_users():
    """
    Get all users from the Traq API.
    """
    return userapi.get_users(include_suspended=True)


def get_user(user_id: str):
    """
    Get a user from the Traq API.
    """
    return userapi.get_user(user_id)
