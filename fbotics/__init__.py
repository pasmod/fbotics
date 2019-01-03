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

    def send_text_message(
            self,
            recipient_id=None,
            text=None,
            user_ref=None,
            phone_number=None):
        """Sends a simple text message to a given recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            text: message to be sent to the recipient
            user_ref: optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.

        # Examples
        ```python
        client.send_text_message(recipient_id="2157136727638083", text="hello world!")
        client.send_text_message(phone_number="+1 (555) 857-6309", text="hello world!")
        client.send_text_message(user_ref="<UNIQUE_REF_PARAM>", text="hello world!")
        ```
        """
        message = Message({"text": text})
        recipient = Recipient(
            {"id": recipient_id, "user_ref": user_ref, "phone_number": phone_number})
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
        """Retrieves the supported tags by Facebook.

        # Examples
        ```python
        client.retrieve_supported_tags()
        ```
        """
        URL = "https://graph.facebook.com/v2.6/page_message_tags"
        params = {'access_token': self.page_access_token}
        response = requests.get(
            URL,
            params=params)
        return response
