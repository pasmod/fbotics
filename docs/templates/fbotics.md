## Usage of FBotics Client

The Send API is the main API used to send messages to users, including text, attachments, structured message templates, sender actions, and more. FBotics implements a client to ease the use of the Send API in Python.

In order to create an instance of the Client, a page access token is needed. 

```python
from fbotics import Client

client = Client(page_access_token="PAGE_ACCESS_TOKEN")
```

## Methods

{{autogenerated}}