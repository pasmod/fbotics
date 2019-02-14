from schematics import Model
from schematics.types import StringType, ListType, PolyModelType, BooleanType

from fbotics.models.buttons import PostbackButton, WebUrlButton, CallButton


def button_claim_function(field, data):
    print("data", data)
    if "url" in data:
        return WebUrlButton
    if "payload" in data and data.get("type") == "postback":
        return PostbackButton
    if "payload" in data and data.get("type") == "phone_number":
        return CallButton
    else:
        return None


class ButtonTemplatePayload(Model):
    """The button template allows you to send a structured message that includes text and buttons.

    # Arguments
        template_type: Value must be button.
        text: UTF-8-encoded text of up to 640 characters. Text will appear above the buttons.
        buttons: Set of 1-3 buttons that appear as call-to-actions.
        sharable: Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false.

    """

    template_type = StringType(required=True, default="button", choices=["button"])
    text = StringType(required=True, max_length=640)
    buttons = ListType(
        PolyModelType(
            [PostbackButton, WebUrlButton, CallButton],
            claim_function=button_claim_function,
        )
    )
    sharable = BooleanType(default=False)
