FROM ubuntu:18.04


EXPOSE 5000

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

ENV SERVER_URL=http://localhost:8200
ENV APP_NAME=flask-apm-client
ENV SERVICE_NAME=Flask-APM-Test

ENV DB_HOST=flask-pony-db
ENV DB_USER=docker
ENV DB_PASS=Test123

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "team.py" ]