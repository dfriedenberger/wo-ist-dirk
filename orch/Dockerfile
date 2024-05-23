FROM python:3.12-slim-bookworm


# Test

RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y mosquitto-clients
RUN apt-get install -y dos2unix

#USER 1000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
COPY subscribe.py subscribe.py
COPY server.py server.py
COPY templates templates
COPY htdocs htdocs


COPY wrapper.sh wrapper.sh
RUN dos2unix wrapper.sh
RUN chmod 0700 wrapper.sh
CMD ./wrapper.sh

