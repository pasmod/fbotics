from pytest_voluptuous import S, Partial


def test_retrieve_supported_tags_response_status_code_is_200(client, recipient_id):
    """
    GIVEN a client
    WHEN retrieving the list of supported tags
    THEN the status code of the response is 200
    """
    response = client.retrieve_supported_tags()
    assert response.status_code == 200


def test_retrieve_supported_tags_response_structure_is_as_expected(client):
    """
    GIVEN a client
    WHEN retrieving the list of supported tags
    THEN the structure of the response is as expected
    """
    response = client.retrieve_supported_tags().json()
    schema = S({"data": Partial([S({"tag": str, "description": str})])})
    assert response == schema
