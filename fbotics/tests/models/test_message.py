import pytest

from fbotics.models.message import Message
from schematics.exceptions import DataError


def test_validation_when_text_of_message_is_too_long(client):
    """
    GIVEN a Message object with a too long text
    WHEN validating the object
    THEN is throws a validation error
    """
    m = Message({"text": "*" * 2001})
    with pytest.raises(DataError):
        m.validate()
