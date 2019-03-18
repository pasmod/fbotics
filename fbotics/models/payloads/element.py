from schematics import Model
from schematics.types import StringType, ListType, ModelType
from schematics.types.compound import PolyModelType

from fbotics.models.buttons import PostbackButton, WebUrlButton


def button_claim_function(field, data):
    if "url" in data:
        return WebUrlButton
    if "payload" in data:
        return PostbackButton
    else:
        return None


class DefaultAction(Model):
    """The default action executed when the template is tapped.

    # Arguments
        type: Type of button. Must be web_url.
        url: This URL is opened in a mobile browser when the button is tapped. Must use HTTPS protocol if messenger_extensions is true.
        webview_height_ratio: Optional. Height of the Webview. Valid values: compact, tall, full. Defaults to full.

    """

    type = StringType(required=True, default="web_url", choices=["web_url"])
    webview_height_ratio = StringType(
        required=False, default="full", choices=["compact", "tall", "full"]
    )
    url = StringType()


class Element(Model):
    """The generic template supports a maximum of 10 elements per message. At least one property must be set in addition to title.

    # Arguments
        title: The title to display in the template. 80 character limit.
        subtitle: Optional. The subtitle to display in the template. 80 character limit.
        image_url: Optional. The URL of the image to display in the template.
        default_action: Optional. The default action executed when the template is tapped. Accepts the same properties as URL button, except title.
        buttons: Optional. An array of buttons to append to the template. A maximum of 3 buttons per element is supported.

    """

    title = StringType(required=True, max_length=80)
    image_url = StringType(required=False, max_length=80)
    subtitle = StringType(required=False)
    default_action = ModelType(DefaultAction, required=False)
    buttons = ListType(
        PolyModelType(
            [PostbackButton, WebUrlButton], claim_function=button_claim_function
        ),
        max_size=3,
    )
