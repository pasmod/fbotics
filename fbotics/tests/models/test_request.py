import pytest

from fbotics.models.request import Request


def test_if_supported_tags_are_valid(client, recipient_id):
    """
    GIVEN a Request object
    WHEN validating the tags property of the object
    THEN is allows only valid and up-to-date choices
    """
    r = Request()
    actual = r.fields["tag"].choices
    expected = [entry["tag"]
                for entry in client.retrieve_supported_tags().json()["data"]]
    assert set(actual) == set(expected)
