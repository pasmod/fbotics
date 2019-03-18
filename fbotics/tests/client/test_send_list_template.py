from fbotics.models.buttons import WebUrlButton
from fbotics.models.payloads.element import Element
from fbotics.models.quick_reply import QuickReply


def test_send_list_template_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a list template is sent to the recipient
    THEN the status code of the response is 200
    """

    buttons = [
        WebUrlButton(
            dict(type="web_url", url="http://www.google.com", title="Web URL Button")
        )
    ]

    e1 = Element(
        dict(
            title="Title1",
            image_url="http://i67.tinypic.com/262vb5l.jpg",
            subtitle="Subtitle1",
            buttons=buttons,
        )
    )

    e2 = Element(
        dict(
            title="Title1",
            image_url="http://i67.tinypic.com/262vb5l.jpg",
            subtitle="Subtitle1",
            buttons=buttons,
        )
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

    response = client.send_list_template(
        recipient_id=recipient_id, quick_replies=[qr1, qr2], elements=[e1, e2], buttons=buttons
    )
    assert response.status_code == 200
