import requests

from fbotics import Request
from fbotics.client.exceptions import OAuthException
from fbotics.models.attachment import Attachment
from fbotics.models.message import Message
from fbotics.models.payloads.button_template import ButtonTemplatePayload
from fbotics.models.payloads.generic_template import GenericTemplatePayload
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
            buttons: Set of 1-3 buttons that appear as call-to-actions.

        """

        generic_template_payload = GenericTemplatePayload(
            dict(template_type="generic", elements=elements)
        )
        attachment = Attachment(dict(type="template", payload=generic_template_payload))
        message = Message({"quick_replies": quick_replies, "attachment": attachment})

        response = self._post(message, recipient_id, user_ref, phone_number)
        return response

    def send_quick_replies(
            self,
            recipient_id=None,
            user_ref=None,
            phone_number=None,
            text=None,
            quick_replies=None
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

    def send(
            self,
            recipient_id=None,
            text=None,
            user_ref=None,
            phone_number=None,
            quick_replies=None,
            attachment=None,
    ):
        """Sends a  message to a given recipient.

        # Arguments
            recipient_id: page specific id of the recipient
            text: message to be sent to the recipient
            user_ref: optional. user_ref from the checkbox plugin
            phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368. Your bot must be approved for Customer Matching to send messages this way.
            quick_replies: An array of objects the describe the quick reply buttons to send. A maximum of 11 quick replies are supported.

        # Examples
        Sending a Text Message
        ```python
            client.send(recipient_id="2157136727638083", text="hello world!")
            client.send(phone_number="+1 (555) 857-6309", text="hello world!")
            client.send(user_ref="<UNIQUE_REF_PARAM>", text="hello world!")
        ```

        Sending Quick Replies
        ```python
            from fbotics.models.quick_reply import QuickReply
            qr1 = QuickReply({"content_type": "text",
                              "title": "Yes",
                              "payload": "payload1",
                              "image_url": "http://i64.tinypic.com/1hothh.png"})
            qr2 = QuickReply({"content_type": "text",
                              "title": "No",
                              "payload": "payload2",
                              "image_url": "http://i63.tinypic.com/2pqpbth.png"})
            quick_replies = [qr1, qr2]
            response = client.send_message(recipient_id=2157136727638083,
                                          text="Text Message with Quick Replies",
                                          quick_replies=quick_replies)
        ```
        """
        message = Message(
            {"text": text, "quick_replies": quick_replies, "attachment": attachment}
        )

        response = self._post(message, recipient_id, user_ref, phone_number)
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
