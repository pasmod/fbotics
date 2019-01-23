from schematics import Model
from schematics.types import StringType, ListType, PolyModelType, BooleanType

from fbotics.models.buttons import PostbackButton, WebUrlButton, CallButton


def button_claim_function(field, data):
    print("data", data)
    if 'url' in data:
        return WebUrlButton
    if 'payload' in data and data.get("type") == "postback":
        return PostbackButton
    if 'payload' in data and data.get("type") == "phone_number":
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

    # Examples
        ```python
            from fbotics.models.payloads.button_template import ButtonTemplatePayload
            b1 = ...
            b2 = ...
            ButtonTemplatePayload(dict(text="What can I do?", buttons=[b1, b2]))
        ```
        <p float="center">
            <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/23204276_131607050888932_1057585862134464512_n.png?_nc_cat=106&_nc_ht=scontent-frx5-1.xx&oh=22abe202e08e4ff2747698761a5b59a7&oe=5CCD030A" width="30%" />
        </p>
    """
    template_type = StringType(required=True, default='button',
                               choices=['button'])
    text = StringType(required=True, max_length=640)
    buttons = ListType(PolyModelType(
        [PostbackButton, WebUrlButton, CallButton], claim_function=button_claim_function))
    sharable = BooleanType(default=False)
