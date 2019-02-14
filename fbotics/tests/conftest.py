import pytest

from fbotics.client import Client


@pytest.fixture(scope="module")
def client():
    return Client(
        page_access_token="EAAHIhFHZCIQIBAAme5oAtHehYfrZCvyUZAMLABGEW8ZBmdZASYFp8wdhtbD3POKbT7m3yOnue9Y2JrYZAZBSVne0yHfdKKKfxrjL1aZB5nFCWVjBZA7BiZBNsMrVhSZCfqi4cB6CZCi2CUh41waGNlIc7gcFxAl421dqoNBUPD5ZAjxiHrAJmDRdYx8ATJRBkRqRhowMZD"
    )


@pytest.fixture(scope="module")
def recipient_id():
    return "2157136727638083"
