The button template allows you to send a structured message that includes text and buttons. This is an example to send Button Templates using FBotics:

```python
from fbotics.client import Client
from fbotics.models.buttons import WebUrlButton, CallButton
from fbotics.models.quick_reply import QuickReply

client = Client(page_access_token=PAGE_ACCESS_TOKEN)

button1 = WebUrlButton(
    dict(type="web_url", url="http://www.google.com", title="Get Order Status")
)
button2 = CallButton(dict(type="phone_number", payload="+15105551234", title="Call Me"))

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

client.send_button_template(
    recipient_id=RECIPIENT_ID,
    text="Hello World",
    quick_replies=[qr1, qr2],
    buttons=[button1, button2],
)
```