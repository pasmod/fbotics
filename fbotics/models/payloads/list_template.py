from schematics import Model
from schematics.types import StringType, ListType, ModelType, BooleanType
from schematics.types.compound import PolyModelType

from fbotics.models.buttons import PostbackButton, WebUrlButton
from fbotics.models.payloads.element import Element


def button_claim_function(field, data):
    if "url" in data:
        return WebUrlButton
    if "payload" in data:
        return PostbackButton
    else:
        return None


class ListTemplatePayload(Model):
    """The list template is a list of 2-4 structured items with an optional global button rendered at the bottom. Each item may contain a thumbnail image, title, subtitle, and one button. You may also specify a default_action object that sets a URL that will be opened in the Messenger webview when the item is tapped.

    # Arguments
        template_type: Value must be list.
        top_element_style: Optional. Sets the format of the first list items. Messenger web client currently only renders compact.
        elements: Array of objects that describe items in the list. Minimum of 2 elements required. Maximum of 4 elements is supported.
        shareable: Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false.
        buttons: Optional. Button to display at the bottom of the list. Maximum of 1 button is supported. 

    """

    template_type = StringType(required=False, default="list", choices=["list"])
    top_element_style = StringType(required=False, default="compact", choices=["compact", "large"])
    elements = ListType(ModelType(Element), min_size=2, max_size=4)
    sharable = BooleanType(default=False)
    buttons = ListType(
        PolyModelType(
            [PostbackButton, WebUrlButton], claim_function=button_claim_function
        ),
        max_size=1,
    )
