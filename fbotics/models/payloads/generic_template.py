from schematics import Model
from schematics.types import StringType, ListType, ModelType, BooleanType

from fbotics.models.buttons import PostbackButton, WebUrlButton
from fbotics.models.payloads.element import Element


def button_claim_function(field, data):
    if "url" in data:
        return WebUrlButton
    if "payload" in data:
        return PostbackButton
    else:
        return None


class GenericTemplatePayload(Model):
    """The generic template is a simple structured message that includes a title, subtitle, image, and up to three buttons. You may also specify a default_action object that sets a URL that will be opened in the Messenger webview when the template is tapped.

    # Arguments
        template_type: Value must be generic.
        sharable: Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false.
        elements: An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.

    """

    template_type = StringType(required=False, default="generic", choices=["generic"])
    sharable = BooleanType(default=False)
    elements = ListType(ModelType(Element), max_size=10)
