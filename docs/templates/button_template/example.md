This is an example to send Button Templates using FBotics:


```python
from fbotics.models.attachment import Attachment
from fbotics.models.buttons import WebUrlButton, CallButton
from fbotics.models.payloads.button_template import ButtonTemplatePayload


button1 = WebUrlButton(
    dict(type="web_url", url="http://www.google.com", title="Get Order Status")
).to_primitive()
button2 = CallButton(
    dict(type="phone_number", payload="+15105551234", title="Call Me")
).to_primitive()
button_template_payload = ButtonTemplatePayload(
    dict(
        template_type="button",
        text="What can I do to help?",
        buttons=[button1, button2],
    )
).to_primitive()
attachment = Attachment(dict(type="template", payload=button_template_payload))
response = client.send_message(recipient_id=recipient_id, attachment=attachment)
```

<p float="center">
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/23204276_131607050888932_1057585862134464512_n.png?_nc_cat=106&_nc_ht=scontent-frx5-1.xx&oh=10032f773b9adf090cc62f4d38145f38&oe=5CF4900A" width="40%" />
</p>