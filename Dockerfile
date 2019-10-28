#https://docs.docker.com/compose/django/
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/static_dev
WORKDIR /code
RUN pip install setuptools
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install python3-yaml
RUN pip install -r requirements.txt
COPY . /code/