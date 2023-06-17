from traq.api.user_api import UserApi
from .traq_api import client
import requests

userapi = UserApi(client)


def get_users():
    """
    Get all users from the Traq API.
    """
    print(f"Bearer {client.configuration.access_token}")
    headers: dict = {
        "Authorization": f"Bearer {client.configuration.access_token}",
        "Content-Type": "application/json",
    }

    res = requests.get(
        "https://q.trap.jp/api/v3/users?include-suspended=true",
        headers=headers,
    )
    if res.status_code == 200:
        return res.json()
    return []


def get_user(user_id: str):
    """
    Get a user from the Traq API.
    """
    return userapi.get_user(user_id)
