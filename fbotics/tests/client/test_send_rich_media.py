from fbotics.models.quick_reply import QuickReply


def test_send_image_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN an image is sent to the recipient
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

    response = client.send_image(
        recipient_id=recipient_id,
        url="http://i63.tinypic.com/2zfprph.png",
        quick_replies=[qr1, qr2],
    )
    assert response.status_code == 200


def test_send_audio_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN an audio is sent to the recipient
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

    response = client.send_audio(
        recipient_id=recipient_id,
        url="http://www.pacdv.com/sounds/voices/mmm-1.wav",
        quick_replies=[qr1, qr2],
    )
    assert response.status_code == 200


def test_send_file_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a file is sent to the recipient
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

    response = client.send_file(
        recipient_id=recipient_id,
        url="http://www.xmlpdf.com/manualfiles/hello-world.pdf",
        quick_replies=[qr1, qr2],
    )
    assert response.status_code == 200
