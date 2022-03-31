FROM python:3.9.0-alpine3.12 
RUN apk add --no-cache bash
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/

