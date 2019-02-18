This is an example to send text messages using FBotics:




```python
from fbotics.client import Client
from fbotics.models.quick_reply import QuickReply

client = Client(page_access_token=PAGE_ACCESS_TOKEN)

response = client.send_text(
    recipient_id=RECIPIENT_ID, text="hello world"
)
```