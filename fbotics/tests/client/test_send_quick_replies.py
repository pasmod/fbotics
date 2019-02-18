from fbotics.models.quick_reply import QuickReply


def test_send_quick_replies_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN quick replies are sent to the recipient
    THEN the status code of the response is 200
    """

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

    response = client.send_quick_replies(
        recipient_id=recipient_id, text="hello world", quick_replies=[qr1, qr2]
    )
    assert response.status_code == 200
