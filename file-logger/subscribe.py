import json
import logging
import random
from datetime import datetime

import configparser
import paho.mqtt.client as mqtt

configParser = configparser.RawConfigParser()
configParser.read('config/subscriber.conf')

config = configParser['default']


# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, _user_data, _flags, reason_code, _properties):
    logging.info(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config['topic'])


# The callback for when a PUBLISH message is received from the server.
def on_message(_client, _user_data, msg):
    logging.info(f"topic:{msg.topic} msg:{str(msg.payload)}")
    topic = "unknown"
    if msg.topic.startswith("owntracks/"):
        topic = "owntracks"

    # validate
    try:
        obj = json.loads(msg.payload)
    except Exception as e:
        logging.error(f"Cannot validate {e}")

    date = datetime.now().strftime("%Y%m%d")
    with open(f"data/{topic}-{date}.jsonl", 'a+', encoding='UTF-8') as f:
        line = json.dumps(obj)
        f.write(f"{line}\n")


def run():
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Started {client_id}')
    client = mqtt.Client(client_id=client_id, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(config['username'], config['password'])

    client.on_connect = on_connect
    client.on_message = on_message

    logging.info(f"Connect to {config['broker']}:{config['port']} with user {config['username']}")
    client.connect(config['broker'], int(config['port']), 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == '__main__':
    run()
