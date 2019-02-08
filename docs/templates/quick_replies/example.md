This is an example to send Quick Replies using FBotics:




```python
from fbotics.models.quick_reply import QuickReply

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
quick_replies = [qr1, qr2]
response = client.send_message(
    recipient_id=recipient_id, text="foo", quick_replies=quick_replies
)
```
        
<p float="center">
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/14175277_1582251242076612_248078259_n.png?_nc_cat=101&_nc_ht=scontent-frx5-1.xx&oh=e24d393b391cb88ab24c2e525b5a8e59&oe=5CE1DCD6" width="90%" />
</p>
