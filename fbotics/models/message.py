from schematics.models import Model
from schematics.types import StringType


# TODO: Add missing fields and constraints
class Message(Model):
    text = StringType(required=True)
