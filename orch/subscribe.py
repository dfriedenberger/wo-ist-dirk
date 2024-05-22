import json
import logging
import random
import paho.mqtt.client as mqtt


config = None
with open('config/subscriber.json', encoding='UTF-8') as f:
    config = json.load(f)

# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    logging.info(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config['topic'])


# The callback for when a PUBLISH message is received from the server.
def on_message(client, user_data, msg):
    logging.info(f"{msg.topic} {client} {user_data} msg:{str(msg.payload)}")


def run():
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Started {client_id}')
    client = mqtt.Client(client_id=client_id, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(config['username'], config['password'])

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config['broker'], config['port'], 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == '__main__':
    run()
