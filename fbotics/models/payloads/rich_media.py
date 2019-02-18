from schematics import Model
from schematics.types import StringType, BooleanType


class RichMediaPayload(Model):
    """The Messenger Platform allows you to attach assets to messages, including audio, video, images, and files.

    # Arguments
        url: The turl of the asset.
        is_reusable: Attachments that were uploaded with the is_reusable property set to true can be sent to other message recipients.

    """

    url = StringType(required=False)
    is_reusable = BooleanType(required=False, serialize_when_none=False)
