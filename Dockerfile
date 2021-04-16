FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y  sqlite3

ADD . /app/
WORKDIR /app

RUN pip install -r requirements.txt
