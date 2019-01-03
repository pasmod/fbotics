from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType

from fbotics.models.message import Message
from fbotics.models.recipient import Recipient


class Request(Model):
    messaging_type = StringType(
        required=True,
        choices=[
            "RESPONSE",
            "MESSAGE_TAG",
            "UPDATE"],
        default="RESPONSE")
    tag = StringType(
        required=False,
        choices=[
            "BUSINESS_PRODUCTIVITY",
            "COMMUNITY_ALERT",
            "CONFIRMED_EVENT_REMINDER",
            "NON_PROMOTIONAL_SUBSCRIPTION",
            "PAIRING_UPDATE",
            "APPLICATION_UPDATE",
            "ACCOUNT_UPDATE",
            "PAYMENT_UPDATE",
            "PERSONAL_FINANCE_UPDATE",
            "SHIPPING_UPDATE",
            "RESERVATION_UPDATE",
            "ISSUE_RESOLUTION",
            "APPOINTMENT_UPDATE",
            "GAME_EVENT",
            "TRANSPORTATION_UPDATE",
            "FEATURE_FUNCTIONALITY_UPDATE",
            "TICKET_UPDATE"])
    recipient = ModelType(Recipient)
    message = ModelType(Message)

    def validate_messaging_type(self, data, value):
        if data["tag"] and data["messaging_type"] != "MESSAGE_TAG":
            raise ValidationError(
                "Messaging type should be MESSAGE_TAG for tagged messages")
        return value
