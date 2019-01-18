from schematics.models import Model
from schematics.types import StringType, BooleanType
from schematics.types.compound import ModelType


class Payload(Model):
    url = StringType(required=False)
    is_reusable = BooleanType(required=False, serialize_when_none=False)


class Attachment(Model):
    type = StringType(required=True, choices=["image", "audio", "video",
                                              "file",
                                              "template"])
    payload = ModelType(Payload, required=True)
