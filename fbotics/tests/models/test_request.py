import pytest

from fbotics.models.request import Request
from schematics.exceptions import DataError


def test_if_supported_tags_are_valid(client):
    """
    GIVEN a Request object
    WHEN validating the tags property of the object
    THEN is allows only valid and up-to-date choices
    """
    r = Request()
    actual = r.fields["tag"].choices
    expected = [
        entry["tag"] for entry in client.retrieve_supported_tags().json()["data"]
    ]
    assert set(actual) == set(expected)


def test_if_having_tag_without_correct_message_type_throws_validation_error():
    """
    GIVEN a Request object with a tag and RESPONSE messaging type
    WHEN validating the request object
    THEN is throws a validation error
    """
    r = Request({"messaging_type": "RESPONSE", "tag": "GAME_EVENT"})
    with pytest.raises(DataError):
        r.validate()
