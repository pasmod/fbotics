from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType


def is_blank(string):
    return not (string and string.strip())


class QuickReply(Model):
    """Represent a message object in a request sent to Facebook.

    # Arguments
        content_type: Must be one of the following text: Sends a text button, location: Sends a button to collect the recipient's location, user_phone_number: Sends a button allowing recipient to send the phone number associated with their account.,user_email: Sends a button allowing recipient to send the email associated with their account.
        title: Required if content_type is 'text'. The text to display on the quick reply button. 20 character limit.
        payload: Required if content_type is 'text'. Custom data that will be sent back to you via the messaging_postbacks webhook event. 1000 character limit. May be set to an empty string if image_url is set.
        image_url: Optional. URL of image to display on the quick reply button for text quick replies. Image should be a minimum of 24px x 24px. Larger images will be automatically cropped and resized. Required if title is an empty string.

    """

    content_type = StringType(
        required=True, choices=["text", "location", "user_phone_number", "user_email"]
    )
    title = StringType(required=False, serialize_when_none=False, max_length=20)
    payload = StringType(required=False, serialize_when_none=False, max_length=1000)
    image_url = StringType(required=False, serialize_when_none=False)

    def validate_content_type(self, data, value):
        if data["content_type"] == "text" and not data["title"]:
            raise ValidationError("Field title is required when content_type is text")
        if (
                data["content_type"] == "text"
                and data["image_url"]
                and not data.get("payload", "")
        ):
            raise ValidationError(
                "When content_type is text and image_url is set, payload should be set to at least an empty string."
            )
        return value

    def validate_image_url(self, data, value):
        if is_blank(data.get("title", None)) and not data["image_url"]:
            raise ValidationError(
                "Field image_url is required if title is an empty string"
            )
        return value
