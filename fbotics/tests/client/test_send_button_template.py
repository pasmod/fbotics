from fbotics.models.buttons import WebUrlButton, CallButton
from fbotics.models.quick_reply import QuickReply


def test_send_button_template_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a button template is sent to the recipient
    THEN the status code of the response is 200
    """

    button1 = WebUrlButton(
        dict(type="web_url", url="http://www.google.com", title="Get Order Status")
    )
    button2 = CallButton(
        dict(type="phone_number", payload="+15105551234", title="Call Me")
    )

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

    response = client.send_button_template(
        recipient_id=recipient_id,
        text="Hello World",
        quick_replies=[qr1, qr2],
        buttons=[button1, button2],
    )
    assert response.status_code == 200
