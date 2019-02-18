
def test_send_text_returns_200_status_code(client, recipient_id):
    """
    GIVEN a client and a recipient id
    WHEN a text message is sent to the recipient
    THEN the status code of the response is 200
    """

    response = client.send_text(
        recipient_id=recipient_id, text="hello world"
    )
    assert response.status_code == 200
