from traq.api.stamp_api import StampApi
from .traq_api import client

stamp_api = StampApi(client)


def get_stamps():
    """
    Get all stamps from the Traq API.
    """
    return stamp_api.get_stamps()
