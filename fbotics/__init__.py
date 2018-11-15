import requests
from fbotics.models.message import Message
from fbotics.models.recipient import Recipient
from fbotics.models.request import Request

API_URL = "https://graph.facebook.com/v2.6/me/messages"


# TODO: Configure logger
class Client(object):
    def __init__(self, page_access_token=None):
        self.page_access_token = page_access_token

    def send_text_message(self, recipient_id=None, text=None):
        message = Message({"text": text})
        recipient = Recipient({"id": recipient_id})
        request = Request({"recipient": recipient, "message": message})
        # Throws an exception is not valid
        request.validate()
        params = {'access_token': self.page_access_token}
        response = requests.post(
            API_URL,
            params=params,
            json=request.to_primitive())
        return response
