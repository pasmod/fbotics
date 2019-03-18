import requests

from fbotics import Request
from fbotics.client.exceptions import OAuthException
from fbotics.models.attachment import Attachment
from fbotics.models.message import Message
from fbotics.models.payloads.button_template import ButtonTemplatePayload
from fbotics.models.payloads.generic_template import GenericTemplatePayload
from fbotics.models.payloads.list_template import ListTemplatePayload
from fbotics.models.payloads.rich_media import RichMediaPayload
from fbotics.models.recipient import Recipient

API_URL = "https://graph.facebook.com/v2.6/me/messages"


class Client(object):
    def __init__(self, page_access_token=None):
        self.page_access_token = page_access_token

    def send_button_template(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            text=None,
            quick_replies=None,
            buttons=None,
    ):
        """Sends a button template to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            text: UTF-8-encoded text of up to 640 characters. Text will appear above the buttons.
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.
            buttons: Set of 1-3 buttons that appear as call-to-actions.

        """

        button_template_payload = ButtonTemplatePayload(
            dict(template_type="button", text=text, buttons=buttons)
        )
        attachment = Attachment(dict(type="template", payload=button_template_payload))
        message = Message({"quick_replies": quick_replies, "attachment": attachment})
        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_generic_template(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            elements=None,
            quick_replies=None,
    ):
        """Sends a generic template to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            elements: An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        """

        generic_template_payload = GenericTemplatePayload(
            dict(template_type="generic", elements=elements)
        )
        attachment = Attachment(dict(type="template", payload=generic_template_payload))
        message = Message({"quick_replies": quick_replies, "attachment": attachment})

        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_list_template(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            elements=None,
            buttons=None,
            quick_replies=None
    ):
        """Sends a list template to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            elements: Array of objects that describe items in the list. Minimum of 2 elements required. Maximum of 4 elements is supported.
            buttons: Button to display at the bottom of the list. Maximum of 1 button is supported.
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        """

        list_template_payload = ListTemplatePayload(
            dict(template_type="list", elements=elements, buttons=buttons)
        )
        attachment = Attachment(dict(type="template", payload=list_template_payload))
        message = Message({"quick_replies": quick_replies, "attachment": attachment})

        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_quick_replies(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            text=None,
            quick_replies=None,
    ):
        """Sends quick replies to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: Optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            text: must be UTF-8 and has a 2000 character limit.
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.


        """

        message = Message({"text": text, "quick_replies": quick_replies})

        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_text(self, recipient_id=None, user_ref=None, phone_number=None, text=None):
        """Sends a text message to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: Optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            text: must be UTF-8 and has a 2000 character limit.


        """

        message = Message({"text": text})

        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_image(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            url=None,
            quick_replies=None,
    ):
        """Sends an image to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: Optional. user_ref from the checkbox plugin
            url: URL of the image
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        """
        attachment = Attachment(
            dict(type="image", payload=RichMediaPayload(dict(url=url)))
        )
        message = Message({"quick_replies": quick_replies, "attachment": attachment})
        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_audio(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            url=None,
            quick_replies=None,
    ):
        """Sends an audio to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: Optional. user_ref from the checkbox plugin
            url: URL of the audio
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        """
        attachment = Attachment(
            dict(type="audio", payload=RichMediaPayload(dict(url=url)))
        )
        message = Message({"quick_replies": quick_replies, "attachment": attachment})
        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_file(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            url=None,
            quick_replies=None,
    ):
        """Sends a file to the recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            user_ref: Optional. user_ref from the checkbox plugin
            url: URL of the file
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        """
        attachment = Attachment(
            dict(type="file", payload=RichMediaPayload(dict(url=url)))
        )
        message = Message({"quick_replies": quick_replies, "attachment": attachment})
        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def retrieve_supported_tags(self):
        """Retrieves the supported tags by Facebook.

        # Examples
        ```python
        client.retrieve_supported_tags()
        ```
        """
        URL = "https://graph.facebook.com/v2.6/page_message_tags"
        params = {"access_token": self.page_access_token}
        response = requests.get(URL, params=params)
        return response

    def _post(self, message, recipient_id=None, user_ref=None, phone_number=None):
        recipient = Recipient(
            {"id": recipient_id, "user_ref": user_ref, "phone_number": phone_number}
        )
        request = Request({"recipient": recipient, "message": message})
        request.validate()
        params = {"access_token": self.page_access_token}
        response = requests.post(API_URL, params=params, json=request.to_primitive())
        json_response = response.json()
        if (
                response.status_code == 400
                and json_response.get("error", {}).get("type", "") == "OAuthException"
        ):
            raise OAuthException(json_response.get("error").get("message", ""))
        return response
