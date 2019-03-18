This is an example to send List Templates using FBotics:

```python
from fbotics.client import Client
from fbotics.models.buttons import WebUrlButton
from fbotics.models.payloads.element Element
from fbotics.models.quick_reply import QuickReply

client = Client(page_access_token=PAGE_ACCESS_TOKEN)


buttons = [
        WebUrlButton(
            dict(type="web_url", url="http://www.google.com", title="Web URL Button")
        )
    ]

e1 = Element(
        dict(
            title="Title1",
            image_url="http://i67.tinypic.com/262vb5l.jpg",
            subtitle="Subtitle1",
            buttons=buttons,
            )
        )

e2 = Element(
        dict(
            title="Title1",
            image_url="http://i67.tinypic.com/262vb5l.jpg",
            subtitle="Subtitle1",
            buttons=buttons,
            )
        )

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

response = client.send_generic_template(
    recipient_id=RECIPIENT_ID,
    quick_replies=[qr1, qr2],
    elements=[e1, e2],
    buttons=buttons
)
```

<p float="center">
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/28126658_223368134877650_2823033985926430720_n.png?_nc_cat=104&_nc_ht=scontent-frx5-1.xx&oh=19307a15df1aea5808ba059de620dd41&oe=5D196422" width="40%" />
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/21201919_1215144078631552_6152307842817720320_n.png?_nc_cat=104&_nc_ht=scontent-frx5-1.xx&oh=ec303f8709bf61895a3ac75ff338025e&oe=5D22406A" width="40%" />
</p>
