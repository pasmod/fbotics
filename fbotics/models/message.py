from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import ListType
from schematics.types import StringType
from schematics.types.compound import ModelType

from fbotics.models.attachment import Attachment
from fbotics.models.quick_reply import QuickReply


class Message(Model):
    """Represent a message object in a request sent to Facebook.

    # Arguments
        text: Message text. Previews will not be shown for the URLs in this field. Use attachment instead. Must be UTF-8 and has a 2000 character limit. text or attachment must be set.
        attachment: attachment object. Previews the URL. Used to send messages with media or Structured Messages. text or attachment must be set.
        quick_replies: Optional. Array of quick_reply to be sent with messages
        metadata: Optional. Custom string that is delivered as a message echo. 1000 character limit.

    """

    text = StringType(required=False, max_length=2000, serialize_when_none=False)
    attachment = ModelType(Attachment, required=False, serialize_when_none=False)
    quick_replies = ListType(ModelType(QuickReply), required=False)
    metadata = StringType(required=False, max_length=1000)

    def validate_text(self, data, value):
        if data["text"] and data["attachment"]:
            raise ValidationError(
                "Fields text and attachment can't be set at the same time."
            )
        return value
