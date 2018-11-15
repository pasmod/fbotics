# FBotics: Python Client for Facebook Send API


#### Quick Start
Build the project and install dependencies

```
make build
```

Run the stack locally
```
make up
```

#### Demo
This is an example of sending a text message to a user
```
from fbotics import Client
client = Client(page_access_token="EAAQQHQvZAn7wBAHju9UsxuqWWcUreBozSf2zePcRZBZAjNoaQdxK4o93U9UwGLPYIgy4ZABwkjH5ZBOm4L3aX1x0x4jLtXt8ZAxe3j9qYLpKWeYA2QfMTFt4lVBNB8QjlY0IlgX92yl6SMxH4uKO1QMCJHHYKZBJy9BqZAEJxApMkAZDZD")
client.send_text_message(recipient_id="1198828066838820", text="hello world!")

```
#### Testing

Test without coverage:

```
$ docker-compose run fbotics python -m pytest fbotics/tests/functional
```
