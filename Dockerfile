FROM aibotics/python3:newest

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt --ignore-installed

# add app
COPY . /usr/src/app

# Make fbotics importable
ENV PYTHONPATH /usr/src/app
