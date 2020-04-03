from schematics import Model
from schematics.types import (
    BooleanType,
    DecimalType,
    IntType,
    ListType,
    ModelType,
    StringType,
)


class Element(Model):
    """Element objects that describe items in the order.

    # Arguments
        title: The name to display for the item.
        subtitle: Optional. The subtitle for the item, usually a brief item description.
        quantity: Optional. The quantity of the item purchased.
        price: The price of the item. For free items, '0' is allowed.
        currency: Optional. The currency of the item price.
        image_url: Optional. The URL of an image to be displayed with the item.

    """

    title = StringType(required=True)
    subtitle = StringType(required=False, serialize_when_none=False)
    quantity = IntType(required=False, serialize_when_none=False)
    price = DecimalType(required=True)
    currency = StringType(required=False, serialize_when_none=False)
    image_url = StringType(required=False, serialize_when_none=False)


class Address(Model):
    """The shipping address of the order.

    # Arguments
        street_1: The street address, line 1.
        street_2: Optional. The street address, line 2.
        city: The city name of the address.
        postal_code: The postal code of the address.
        state: The state abbreviation for U.S. addresses, or the region/province for non-U.S. addresses.
        country: The two-letter country abbreviation of the address.

    """

    street_1 = StringType(required=True)
    street_2 = StringType(required=False, serialize_when_none=False)
    city = StringType(required=True)
    postal_code = StringType(required=True)
    state = StringType(required=True)
    country = StringType(required=True)


class Adjustment(Model):
    """Describes payment adjustments, such as discounts.

    # Arguments
        name: Required if the adjustments array is set. Name of the adjustment.
        amount: Required if the adjustments array is set. The amount of the adjustment.

    """

    name = StringType(required=True)
    amount = DecimalType(required=False, serialize_when_none=False)


class Summary(Model):
    """The property values of the summary object should be valid, well-formatted decimal numbers, using '.' (dot) as the decimal separator. Please note that most currencies only accept up to 2 decimal places.

    # Arguments
        subtotal: Optional. The sub-total of the order.
        shipping_cost: Optional. The shipping cost of the order.
        total_tax: Optional. The tax of the order.
        total_cost: The total cost of the order, including sub-total, shipping, and tax.

    """

    subtotal = DecimalType(required=False, serialize_when_none=False)
    shipping_cost = DecimalType(required=False, serialize_when_none=False)
    total_tax = DecimalType(required=False, serialize_when_none=False)
    total_cost = DecimalType(required=True)


class ReceiptTemplatePayload(Model):
    """The receipt template allows you to send an order confirmation as a structured message. The template may include an order summary, payment details, and shipping information.

    # Arguments
        template_type: Value must be receipt.
        sharable: Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false.
        recipient_nam: The recipient's name.
        merchant_name: Optional. The merchant's name. If present this is shown as logo text.
        order_number: The order number. Must be unique.
        currency: The currency of the payment.
        payment_method: The payment method used. Providing enough information for the customer to decipher which payment method and account they used is recommended. This can be a custom string, such as, "Visa 1234".
        timestamp: Optional. Timestamp of the order in seconds.
        elements: Optional. Array of a maximum of 100 element objects that describe items in the order. Sort order of the elements is not guaranteed.
        address: Optional. The shipping address of the order.
        summary: The payment summary. See summary.
        adjustments: Optional. An array of payment objects that describe payment adjustments, such as discounts.

    """

    template_type = StringType(required=True, default="receipt", choices=["receipt"])
    sharable = BooleanType(required=False, default=False, serialize_when_none=False)
    recipient_name = StringType(required=True)
    order_number = StringType(required=True)
    currency = StringType(required=True)
    payment_method = StringType(required=True)
    timestamp = StringType(required=False, serialize_when_none=False)
    elements = ListType(
        ModelType(Element), max_size=100, required=False, serialize_when_none=False
    )
    address = ModelType(Address, required=False, serialize_when_none=False)
    summary = ModelType(Summary, required=True)
    adjustments = ListType(
        ModelType(Adjustment), required=False, serialize_when_none=False
    )
