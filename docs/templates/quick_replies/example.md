This is an example to send Quick Replies using FBotics:




```python
from fbotics.client import Client
from fbotics.models.quick_reply import QuickReply

client = Client(page_access_token=PAGE_ACCESS_TOKEN)

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
    recipient_id=RECIPIENT_ID, text="hello world", quick_replies=[qr1, qr2]
)
```