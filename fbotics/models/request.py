from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType

from fbotics.models.message import Message
from fbotics.models.recipient import Recipient


# TODO: Add missing fields and constraints
class Request(Model):
    messaging_type = StringType(required=True, default="RESPONSE")
    recipient = ModelType(Recipient)
    message = ModelType(Message)
