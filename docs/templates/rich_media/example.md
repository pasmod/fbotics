This is an example to send rich media using FBotics:

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

response = client.send_image(
    recipient_id=RECIPIENT_ID, url="http://i63.tinypic.com/2zfprph.png", quick_replies=[qr1, qr2]
)

response = client.send_audio(
        recipient_id=recipient_id, url="http://www.pacdv.com/sounds/voices/mmm-1.wav", quick_replies=[qr1, qr2]
    )
    
response = client.send_file(
        recipient_id=recipient_id, url="http://www.xmlpdf.com/manualfiles/hello-world.pdf", quick_replies=[qr1, qr2]
    )

```