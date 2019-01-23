import pytest

from fbotics import OAuthException
from fbotics.models.attachment import Attachment
from fbotics.models.buttons import WebUrlButton, CallButton
from fbotics.models.payloads.button_template import ButtonTemplatePayload
from fbotics.models.payloads.generic_template import GenericElement, GenericDefaultAction
from fbotics.models.payloads.generic_template import GenericTemplatePayload
from fbotics.models.payloads.rich_media import RichMediaPayload
from fbotics.models.quick_reply import QuickReply
from fbotics.tests import ANY


def test_status_code_when_sending_text_message_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """
    response = client.send_message(recipient_id=recipient_id, text="foo")
    assert response.status_code == 200


def test_exception_when_sending_text_message_to_invalid_recipient(client):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """
    invalid_recipient_id = 1234
    with pytest.raises(OAuthException):
        client.send_message(recipient_id=invalid_recipient_id, text="foo")


def test_response_content_when_sending_text_message_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """
    response = client.send_message(recipient_id=recipient_id, text="foo")
    assert response.json() == {
        "recipient_id": "2157136727638083",
        "message_id": ANY(str)}


def test_sending_text_message_with_quick_replies_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a text message with quick replies is sent to the recipient
    THEN the status code of the response is 200
    """
    qr1 = QuickReply({"content_type": "text",
                      "title": "Yes",
                      "payload": "payload1",
                      "image_url": "http://i64.tinypic.com/1hothh.png"})
    qr2 = QuickReply({"content_type": "text",
                      "title": "No",
                      "payload": "payload2",
                      "image_url": "http://i63.tinypic.com/2pqpbth.png"})
    quick_replies = [qr1, qr2]
    response = client.send_message(
        recipient_id=recipient_id,
        text="foo",
        quick_replies=quick_replies)
    assert response.status_code == 200


def test_sending_attachment_with_image_url_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN an attachment with an image url is sent to the recipient
    THEN the status code of the response is 200
    """
    attachment = Attachment({"type": "image", "payload": RichMediaPayload(
        {"url": "http://i63.tinypic.com/2zfprph.png"}).to_primitive()})
    response = client.send_message(
        recipient_id=recipient_id,
        attachment=attachment)
    assert response.status_code == 200


def test_sending_attachment_with_audio_url_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN an attachment with an audio url is sent to the recipient
    THEN the status code of the response is 200
    """
    attachment = Attachment({"type": "audio", "payload": RichMediaPayload(
        {"url": "http://www.pacdv.com/sounds/voices/mmm-1.wav"}).to_primitive()})
    response = client.send_message(
        recipient_id=recipient_id,
        attachment=attachment)
    assert response.status_code == 200


def test_sending_attachment_with_file_url_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN an attachment with a file url is sent to the recipient
    THEN the status code of the response is 200
    """
    attachment = Attachment({"type": "file", "payload": RichMediaPayload(
        {"url": "http://www.xmlpdf.com/manualfiles/hello-world.pdf"}).to_primitive()})
    response = client.send_message(
        recipient_id=recipient_id,
        attachment=attachment)
    assert response.status_code == 200


def test_sending_generic_template__to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a generic template is sent to the recipient
    THEN the status code of the response is 200
    """
    generic_default_action = GenericDefaultAction(
        {
            "type": "web_url",
            "url": "http://www.google.com",
            "webview_height_ratio": "compact"}).to_primitive()
    buttons = [WebUrlButton({"type": "web_url",
                             "url": "http://www.google.com",
                             "title": "Web URL Button"}).to_primitive()]
    ge = GenericElement({"title": "Title1",
                         "image_url": "http://i67.tinypic.com/262vb5l.jpg",
                         "subtitle": "Subtitle1",
                         "default_action": generic_default_action,
                         "buttons": buttons}).to_primitive()
    generic_template_payload = GenericTemplatePayload(
        {"template_type": "generic", "elements": [ge]}).to_primitive()
    attachment = Attachment(
        {"type": "template", "payload": generic_template_payload})
    response = client.send_message(
        recipient_id=recipient_id,
        attachment=attachment)
    assert response.status_code == 200


def test_sending_button_template_to_valid_recipient(
        client,
        recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a button template is sent to the recipient
    THEN the status code of the response is 200
    """
    button1 = WebUrlButton({"type": "web_url",
                            "url": "http://www.google.com",
                            "title": "Get Order Status"}).to_primitive()
    button2 = CallButton({"type": "phone_number",
                          "payload": "+15105551234",
                          "title": "Call Me"}).to_primitive()
    button_template_payload = ButtonTemplatePayload(
        {
            "template_type": "button",
            "text": "What can I do to help?",
            "buttons": [
                button1,
                button2]}).to_primitive()
    attachment = Attachment(
        {"type": "template", "payload": button_template_payload})
    print(attachment.to_primitive())
    response = client.send_message(
        recipient_id=recipient_id,
        attachment=attachment)
    assert response.status_code == 200
