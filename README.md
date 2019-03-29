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

## Features
FBotics currently supports sending following message types:

- Quick Replies
- Buttons
    - Call Button
    - Postback Button
    - URL Button
- Templates
    - Button Template
    - Generic Template
    - List Template
    - Receipt Template

Read the documentation at [Fbotics.io](https://pasmod.github.io/fbotics/).
    
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
