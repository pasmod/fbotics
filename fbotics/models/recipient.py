from schematics.models import Model
from schematics.types import StringType


# TODO: Add missing fields and constraints
class Recipient(Model):
    id = StringType(required=False, serialize_when_none=False)
    phone_number = StringType(required=False, serialize_when_none=False)
    user_ref = StringType(required=False, serialize_when_none=False)
