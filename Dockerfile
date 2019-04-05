#https://docs.docker.com/compose/django/
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./var /code/
RUN pip install setuptools
RUN python var/django-localflavor-master/setup.py install
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/