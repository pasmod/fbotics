from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import PolyModelType

from fbotics.models.payloads.button_template import ButtonTemplatePayload
from fbotics.models.payloads.generic_template import GenericTemplatePayload
from fbotics.models.payloads.list_template import ListTemplatePayload
from fbotics.models.payloads.rich_media import RichMediaPayload


def payload_claim_function(field, data):
    if "url" in data and field.name == "payload":
        return RichMediaPayload
    if "top_element_style" in data and field.name == "payload":
        return ListTemplatePayload
    if "elements" in data and field.name == "payload":
        return GenericTemplatePayload
    if "text" in data and field.name == "payload":
        return ButtonTemplatePayload
    else:
        return None


class Attachment(Model):
    """The following can be included in the attachment object: Rich media messages including images, audios, videos, or files and Templates including generic template, button template, receipt template, or list template.

    # Arguments
        type: Type of attachment, may be image, audio, video, file or template. For assets, max file size is 25MB.
        payload: Payload of attachment

    """

    type = StringType(
        required=True, choices=["image", "audio", "video", "file", "template"]
    )
    payload = PolyModelType(
        [RichMediaPayload, GenericTemplatePayload, ButtonTemplatePayload, ListTemplatePayload],
        claim_function=payload_claim_function,
    )
