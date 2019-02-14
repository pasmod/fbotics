from schematics.models import Model
from schematics.types import StringType


class WebUrlButton(Model):
    """The URL Button opens a webpage in the Messenger webview. This button can be used with the Button and Generic Templates.

    # Arguments
        type: Type of button, which is web_url.
        title: Button title. 20 character limit.
        webview_height_ratio: Optional. Height of the Webview. Valid values: compact, tall, full. Defaults to full.
        url: This URL is opened in a mobile browser when the button is tapped. Must use
         HTTPS protocol if messenger_extensions is true.

    # Examples
        ```python
            from fbotics.models.buttons import WebUrlButton
            WebUrlButton(dict(title="hello", url="http://www.google.de"))
        ```
        ![WebUrlButton](https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/17531046_119179685297959_5232300000901332992_n.png?_nc_cat=108&_nc_ht=scontent-frx5-1.xx&oh=bdbdcdee9438decf565412855582046c&oe=5CB66C96)
    """

    type = StringType(required=True, default="web_url", choices=["web_url"])
    title = StringType(required=True, max_length=20)
    webview_height_ratio = StringType(
        required=False, default="full", choices=["compact", "tall", "full"]
    )
    url = StringType()


class CallButton(Model):
    """The call button dials a phone number when tapped. Phone number should be in the format +<COUNTRY_CODE><PHONE_NUMBER>, e.g. +15105559999.

    # Arguments
        type: Type of button, which is phone_number.
        title: Button title, 20 character limit.
        payload: Format must have "+" prefix followed by the country code, area code and local number. For example, +16505551234.

    # Examples
        ```python
            from fbotics.models.buttons import CallButton
            CallButton(dict(title="Call Representative", payload="+15105551234"))
        ```
        <p float="center">
            <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/23204380_457498987984596_8630782823361413120_n.png?_nc_cat=105&_nc_ht=scontent-frx5-1.xx&oh=5fa24ef1529559b5c076dee459ade296&oe=5CB30ECD" width="30%" />
            <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/23083335_129855331000571_3474293560784715776_n.png?_nc_cat=111&_nc_ht=scontent-frx5-1.xx&oh=e2a2a30b526f8c8046de6afa42629d35&oe=5CCCF01F" width="30%" />
        </p>
    """

    type = StringType(default="phone_number", choices=["phone_number"])
    title = StringType(required=True, max_length=20)
    payload = StringType()


class PostbackButton(Model):
    """The postback button sends a messaging_postbacks event to your webhook with the string set in the payload property. This allows you to take an arbitrary actions when the button is tapped. For example, you might display a list of products, then send the product ID in the postback to your webhook, where it can be used to query your database and return the product details as a structured message.

    # Arguments
        type: Type of button, which is postback.
        title: Button title. 20 character limit.
        payload: This data will be sent back to your webhook. 1000 character limit.

    # Examples
        ```python
            from fbotics.models.buttons import PostbackButton
            PostbackButton(dict(title="Select Product", payload="a4f8#4k3"))
        ```
    """

    type = StringType(default="postback", choices=["postback"])
    title = StringType(required=True, max_length=20)
    payload = StringType(required=True, max_length=1000)
