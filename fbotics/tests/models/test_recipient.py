import pytest
from schematics.exceptions import DataError

from fbotics.models.recipient import Recipient


def test_validation_when_id_and_phone_number_are_both_set(client):
    """
    GIVEN a Recipient object with id and phone_number
    WHEN validating the object
    THEN is throws a validation error
    """
    r = Recipient({"id": "foo", "phone_number": "xxx"})
    with pytest.raises(DataError):
        r.validate()


def test_validation_when_user_ref_and_phone_number_are_both_set(client):
    """
    GIVEN a Recipient object with user_ref and phone_number
    WHEN validating the object
    THEN is throws a validation error
    """
    r = Recipient({"phone_number": "xxx", "user_ref": "bar"})
    with pytest.raises(DataError):
        r.validate()


def test_validation_when_id_and_user_ref_are_both_set(client):
    """
    GIVEN a Recipient object with user_ref and id
    WHEN validating the object
    THEN is throws a validation error
    """
    r = Recipient({"id": "foo", "user_ref": "bar"})
    with pytest.raises(DataError):
        r.validate()
