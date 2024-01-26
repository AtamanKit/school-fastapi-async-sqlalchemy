FROM python:3.11-alpine

RUN mkdir /backend
WORKDIR /backend

RUN apk add --no-cache postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
