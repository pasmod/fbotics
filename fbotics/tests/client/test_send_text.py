import pytest

from fbotics.client.exceptions import OAuthException
from fbotics.tests import ANY


def test_send_text_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """

    response = client.send_text(recipient_id=recipient_id, text="hello world")
    assert response.status_code == 200


def test_exception_when_sending_text_message_to_invalid_recipient(client):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """
    invalid_recipient_id = 1234
    with pytest.raises(OAuthException):
        client.send_text(recipient_id=invalid_recipient_id, text="foo")


def test_response_content_when_sending_text_message_to_valid_recipient(
        client, recipient_id
):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """
    response = client.send_text(recipient_id=recipient_id, text="foo")
    assert response.json() == {
        "recipient_id": "2157136727638083",
        "message_id": ANY(str),
    }
