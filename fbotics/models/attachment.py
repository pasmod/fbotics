from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import PolyModelType

from fbotics.models.payloads.button_template import ButtonTemplatePayload
from fbotics.models.payloads.generic_template import GenericTemplatePayload
from fbotics.models.payloads.rich_media import RichMediaPayload


def payload_claim_function(field, data):
    if 'url' in data and field.name == 'payload':
        return RichMediaPayload
    if 'elements' in data and field.name == 'payload':
        return GenericTemplatePayload
    if 'text' in data and field.name == 'payload':
        return ButtonTemplatePayload
    else:
        return None


class Attachment(Model):
    type = StringType(
        required=True,
        choices=[
            "image",
            "audio",
            "video",
            "file",
            "template"])
    payload = PolyModelType([RichMediaPayload,
                             GenericTemplatePayload,
                             ButtonTemplatePayload],
                            claim_function=payload_claim_function)
