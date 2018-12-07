# FBotics: Python Client for Facebook Send API

Read the documentation at [Fbotics.io](https://pasmod.github.io/fbotics/).


## Overview
------------------

FBotics is a Python client for Facebook Send API. The goal of this project is to privide a clean and professional
client, which can be used in production environments. For this, each new functionality added will be fully tested and
documented. Currently this project is under development and offers a limited set of features of the Facebook Send API.

## Getting started: 30 seconds to FBotics
------------------

This is an example of sending a text message to a user
```
from fbotics import Client
client = Client(page_access_token="EAAQQHQvZAn7wBAHju9UsxuqWWcUreBozSf2zePcRZBZAjNoaQdxK4o93U9UwGLPYIgy4ZABwkjH5ZBOm4L3aX1x0x4jLtXt8ZAxe3j9qYLpKWeYA2QfMTFt4lVBNB8QjlY0IlgX92yl6SMxH4uKO1QMCJHHYKZBJy9BqZAEJxApMkAZDZD")
client.send_text_message(recipient_id="1198828066838820", text="hello world!")

```

## Installation
------------------

You can install FBotics from GitHub source:

First, clone FBotics using `git`:

```sh
git clone git@github.com:pasmod/fbotics.git
```

Then, `cd` to the project folder and run the install command:
```sh
cd fbotics
pip install .
```

## Development & Testing
------------------

Before developing FBotics further, please install Docker. For building the Docker image and installing all dependencies
of FBotics, run:

```sh
cd fbotics
make build
```

Then execute the following command to run all the components required to work on FBotics:

```sh
cd fbotics
make up
```

To execute the tests:

```sh
make test
```
