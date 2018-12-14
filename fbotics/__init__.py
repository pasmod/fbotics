import requests

from fbotics.models.message import Message
from fbotics.models.recipient import Recipient
from fbotics.models.request import Request
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

API_URL = "https://graph.facebook.com/v2.6/me/messages"


class OAuthException(Exception):
    pass


# TODO: Configure logger
class Client(object):
    def __init__(self, page_access_token=None):
        self.page_access_token = page_access_token

    def send_text_message(self, recipient_id=None, text=None):
        message = Message({"text": text})
        recipient = Recipient({"id": recipient_id})
        request = Request({"recipient": recipient, "message": message})
        # throws DataError if validation fails
        request.validate()
        params = {'access_token': self.page_access_token}
        response = requests.post(
            API_URL,
            params=params,
            json=request.to_primitive())
        json_response = response.json()
        if response.status_code == 400 and json_response.get(
                "error", {}).get("type", "") == "OAuthException":
            raise OAuthException(json_response.get("error").get("message", ""))
        return response

    def retrieve_supported_tags(self):
        URL = "https://graph.facebook.com/v2.6/page_message_tags"
        params = {'access_token': self.page_access_token}
        response = requests.get(
            URL,
            params=params)
        return response
