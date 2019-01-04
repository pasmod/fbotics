from schematics.models import Model
from schematics.types import ListType
from schematics.types import StringType
from schematics.types.compound import ModelType

from fbotics.models.quick_reply import QuickReply


class Message(Model):
    text = StringType(required=True, max_length=2000)
    quick_replies = ListType(ModelType(QuickReply), required=False)
