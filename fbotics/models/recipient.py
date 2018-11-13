from schematics.models import Model
from schematics.types import StringType


# TODO: Add missing fields and constraints
class Recipient(Model):
    id = StringType(required=True)
    phone_number = StringType(required=False)
    user_ref = StringType(required=False)
