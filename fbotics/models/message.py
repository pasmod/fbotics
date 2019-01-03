from schematics.models import Model
from schematics.types import StringType


class Message(Model):
    text = StringType(required=True, max_length=2000)
