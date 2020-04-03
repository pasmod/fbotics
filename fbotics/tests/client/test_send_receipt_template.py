from fbotics.models.payloads.receipt_template import (
    Address,
    Adjustment,
    Element,
    Summary,
)
from fbotics.models.quick_reply import QuickReply


def test_send_receipt_template_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a receipt template is sent to the recipient
    THEN the status code of the response is 200
    """

    e1 = Element(
        dict(
            title="Classic White T-Shirt",
            subtitle="100% Soft and Luxurious Cotton",
            quantity=2,
            price=50,
            currency="USD",
            image_url="http://petersapparel.parseapp.com/img/whiteshirt.png",
        )
    )

    e2 = Element(
        dict(
            title="Classic Gray T-Shirt",
            subtitle="100% Soft and Luxurious Cotton",
            quantity=1,
            price=25,
            currency="USD",
            image_url="http://petersapparel.parseapp.com/img/grayshirt.png",
        )
    )

    address = Address(
        dict(
            street_1="1 Hacker Way",
            street_2="",
            city="Menlo Park",
            postal_code="94025",
            state="CA",
            country="US",
        )
    )

    summary = Summary(
        dict(subtotal=75.00, shipping_cost=4.95, total_tax=6.19, total_cost=56.14)
    )

    adjustments = [
        Adjustment(dict(name="New Customer Discount", amount=20)),
        Adjustment(dict(name="$10 Off Coupon", amount=10)),
    ]

    qr1 = QuickReply(
        dict(
            content_type="text",
            title="Yes",
            payload="payload1",
            image_url="http://i64.tinypic.com/1hothh.png",
        )
    )

    qr2 = QuickReply(
        dict(
            content_type="text",
            title="No",
            payload="payload2",
            image_url="http://i63.tinypic.com/2pqpbth.png",
        )
    )

    response = client.send_receipt_template(
        recipient_id=recipient_id,
        quick_replies=[qr1, qr2],
        elements=[e1, e2],
        recipient_name="Stephane Crozatier",
        order_number="12345678902",
        currency="USD",
        payment_method="Visa 2345",
        timestamp="1428444852",
        address=address,
        summary=summary,
        adjustments=adjustments,
    )
    assert response.status_code == 200
