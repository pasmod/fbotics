This is an example to send Generic Templates using FBotics:

```python
from fbotics.client import Client
from fbotics.models.buttons import WebUrlButton
from fbotics.models.payloads.generic_template import (
    GenericElement,
)
from fbotics.models.quick_reply import QuickReply

client = Client(page_access_token=PAGE_ACCESS_TOKEN)


buttons = [
        WebUrlButton(
            dict(type="web_url", url="http://www.google.com", title="Web URL Button")
        )
    ]

ge = GenericElement(
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
    elements=[ge],
)
```

<p float="center">
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/22880422_1740199342956641_1916832982102966272_n.png?_nc_cat=107&_nc_ht=scontent-frx5-1.xx&oh=310487994971cafb35b23618567ef34c&oe=5CF2013C" width="40%" />
</p>