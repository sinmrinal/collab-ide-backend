FROM alpine:latest

EXPOSE 8080

WORKDIR /home

RUN apk add build-base

RUN apk add python3

RUN apk add py3-pip

RUN apk add openjdk8-jre

RUN apk add go

RUN apk add rust

COPY . .

ARG token

ENV TOKEN=$token

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]