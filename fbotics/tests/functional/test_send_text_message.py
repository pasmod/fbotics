def test_root_route(client):
    """
    GIVEN a flask application
    WHEN the '/' route is requested
    THEN check that the response is valid
    """
    recipient_id = "2157136727638083"
    response = client.send_text_message(recipient_id=recipient_id, text="foo")
    assert response.status_code == 200
