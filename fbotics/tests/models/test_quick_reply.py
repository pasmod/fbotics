import pytest
from schematics.exceptions import DataError

from fbotics.models.quick_reply import QuickReply


def test_validation_when_content_type_is_text_and_title_does_not_exist(client):
    """
    GIVEN a QuickReply object with a text content type and not title
    WHEN validating the object
    THEN is throws a validation error
    """
    qr = QuickReply({"content_type": "text"})
    with pytest.raises(DataError):
        qr.validate()


def test_validation_when_content_type_is_text_and_image_url_is_set_but_payload_is_not_set(
        client
):
    """
    GIVEN a QuickReply object with a text content type and an image url, but without a payload
    WHEN validating the object
    THEN is throws a validation error
    """
    qr = QuickReply({"content_type": "text", "image_url": "xxx"})
    with pytest.raises(DataError):
        qr.validate()


def test_validation_when_content_type_is_text_and_title_is_empty_and_image_url_is_not_set(
        client
):
    """
    GIVEN a QuickReply object with a text content type and an empty title, but without an image_url
    WHEN validating the object
    THEN is throws a validation error
    """
    qr = QuickReply({"content_type": "text", "title": ""})
    with pytest.raises(DataError):
        qr.validate()
