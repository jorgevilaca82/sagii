#https://docs.docker.com/compose/django/
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/static_dev
WORKDIR /code
RUN pip install setuptools
COPY requirements.txt /code/
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install python3-yaml
RUN apt-get install yarn
RUN pip install -r requirements.txt
COPY . /code/