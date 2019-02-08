This is an example to send Generic Templates using FBotics:

```python
from fbotics.models.payloads.generic_template import GenericTemplatePayload
from fbotics.models.payloads.generic_template import (
    GenericElement,
    GenericDefaultAction,
)
from fbotics.models.attachment import Attachment
from fbotics.models.buttons import WebUrlButton

generic_default_action = GenericDefaultAction(
    dict(type="web_url", url="http://www.google.com", webview_height_ratio="compact")
).to_primitive()
buttons = [
    WebUrlButton(
        dict(type="web_url", url="http://www.google.com", title="Web URL Button")
    ).to_primitive()
]
ge = GenericElement(
    dict(
        title="Title1",
        image_url="http://i67.tinypic.com/262vb5l.jpg",
        subtitle="Subtitle1",
        default_action=generic_default_action,
        buttons=buttons,
    )
).to_primitive()
generic_template_payload = GenericTemplatePayload(
    dict(template_type="generic", elements=[ge])
).to_primitive()
attachment = Attachment(dict(type="template", payload=generic_template_payload))
response = client.send_message(recipient_id=recipient_id, attachment=attachment)
```

<p float="center">
    <img src="https://scontent-frx5-1.xx.fbcdn.net/v/t39.2365-6/22880422_1740199342956641_1916832982102966272_n.png?_nc_cat=107&_nc_ht=scontent-frx5-1.xx&oh=310487994971cafb35b23618567ef34c&oe=5CF2013C" width="40%" />
</p>