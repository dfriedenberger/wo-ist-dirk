FROM python:3.12-slim-bookworm


# Test

RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y mosquitto-clients

#USER 1000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
COPY subscribe.py subscribe.py
CMD [ "python", "./subscribe.py"]