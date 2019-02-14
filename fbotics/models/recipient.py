from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType


class Recipient(Model):
    """Model for the recipient of a message. All requests must include one of id, phone_number, or user_ref.

    # Arguments
        id: Either PSID, phone_number, or user_ref of the message recipient.
        phone_number: Optional. Phone number of the recipient with the format +1(212)555-2368.
        user_ref: Optional. user_ref from the checkbox plugin.
        name: Optional. Used only if phone_number is set. Specifies the person's name in the format: {"first_name":"John", "last_name":"Doe"}

    """

    id = StringType(required=False, serialize_when_none=False)
    phone_number = StringType(required=False, serialize_when_none=False)
    user_ref = StringType(required=False, serialize_when_none=False)
    name = StringType(required=False, serialize_when_none=False)

    def validate_id(self, data, value):
        if data["id"] and (data["phone_number"] or data["user_ref"]):
            raise ValidationError(
                "All requests must include one of id, phone_number, or user_ref"
            )
        return value

    def validate_user_ref(self, data, value):
        if data["user_ref"] and (data["id"] or data["phone_number"]):
            raise ValidationError(
                "All requests must include one of id, phone_number, or user_ref"
            )
        return value

    def validate_phone_number(self, data, value):
        if data["phone_number"] and (data["id"] or data["user_ref"]):
            raise ValidationError(
                "All requests must include one of id, phone_number, or user_ref"
            )
        return value
