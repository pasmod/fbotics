from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType


def is_blank(string):
    return not (string and string.strip())


class QuickReply(Model):
    content_type = StringType(
        required=True,
        choices=[
            "text",
            "location",
            "user_phone_number",
            "user_email"])
    title = StringType(
        required=False,
        serialize_when_none=False,
        max_length=20)
    payload = StringType(
        required=False,
        serialize_when_none=False,
        max_length=1000)
    image_url = StringType(required=False, serialize_when_none=False)

    def validate_content_type(self, data, value):
        if data["content_type"] == "text" and not data["title"]:
            raise ValidationError(
                "Field title is required when content_type is text")
        if data["content_type"] == "text" and data["image_url"] and not data.get(
                "payload", ""):
            raise ValidationError(
                "When content_type is text and image_url is set, payload should be set to at least an empty string.")
        return value

    def validate_image_url(self, data, value):
        if is_blank(data.get("title", None)) and not data["image_url"]:
            raise ValidationError(
                "Field image_url is required if title is an empty string")
        return value
