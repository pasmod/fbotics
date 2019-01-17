# FBotics: Python Client for Facebook Send API

[![Build Status](https://travis-ci.org/pasmod/fbotics.svg?branch=master)](https://travis-ci.org/pasmod/fbotics)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/pasmod/fbotics/blob/master/LICENSE.txt)
[![codecov](https://codecov.io/gh/pasmod/fbotics/branch/master/graph/badge.svg)](https://codecov.io/gh/pasmod/fbotics)
[![pypi](https://img.shields.io/pypi/v/fbotics.svg)](https://pypi.org/project/fbotics/)


Read the documentation at [Fbotics.io](https://pasmod.github.io/fbotics/).


## Overview

FBotics is a Python client for Facebook Send API. The Send API is the main API used to send messages to users, including text,
attachments, structured message templates, sender actions, and more. The goal of this project is to privide a clean and professional
client, which can be used in production environments. For this, each new functionality added will be fully tested and
documented. Currently this project is under development and offers a limited set of features of the Facebook Send API.

## Getting started

First create an instance of the client with the access token of your Facebook page:
```python
from fbotics import Client
client = Client(page_access_token="EAAHIhFHZCIQIBAAme5oAtHehYfrZCvyUZAMLABGEW8ZBmdZASYFp8wdhtbD3POKbT7m3yOnue9Y2JrYZAZBSVne0yHfdKKKfxrjL1aZB5nFCWVjBZA7BiZBNsMrVhSZCfqi4cB6CZCi2CUh41waGNlIc7gcFxAl421dqoNBUPD5ZAjxiHrAJmDRdYx8ATJRBkRqRhowMZD")
```

#### Sending a Text Message
```python
client.send_message(recipient_id="2157136727638083", text="hello world!")
```

![TextMessagey](http://i65.tinypic.com/20f95q1.png)

#### Sending Quick Replies
```python
from fbotics.models.quick_reply import QuickReply
qr1 = QuickReply({"content_type": "text",
                  "title": "Yes",
                  "payload": "payload1",
                  "image_url": "http://i64.tinypic.com/1hothh.png"})
qr2 = QuickReply({"content_type": "text",
                  "title": "No",
                  "payload": "payload2",
                  "image_url": "http://i63.tinypic.com/2pqpbth.png"})
quick_replies = [qr1, qr2]
response = client.send_message(
        recipient_id=2157136727638083,
        text="Text Message with Quick Replies",
        quick_replies=quick_replies)
```

![QuickReply](http://i64.tinypic.com/33myeyu.png)

## Installation

You can install the latest version of FBotics using pip:
```sh
pip install fbotics
```

You can also install FBotics from GitHub source:

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

To create coverage report:

```sh
make coverage
```

