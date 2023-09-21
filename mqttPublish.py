import multiprocessing
import csv
import sys

import paho.mqtt.client as mqtt
from parSensorController import ParSensorController

class mqttPublish():
    def __init__(self):
        return

    def initialise(self):
        client = mqtt.Client(client_id="onpar", protocol=mqtt.MQTTv311)

        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_connect = on_connect

        client.username_pw_set(username="igstest", password="testigs18")
        client.connect(host="51.141.82.199", port=1883)
        client.loop_forever()

        send_message_string(client)

def send_message_string(client):
    x=42
    y=26
    client.publish("cmd/plc/onpar/position", '{{"X":{},"Y":{}}}'.format(x, y), qos=1)


def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))
    client.subscribe("dt/plc/onpar/inposition", qos=0)

def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    return


def on_message(client, userdata, message):
    print("Received event: ", message.payload)

def on_subscribe(client, userdata, mid, qos):
    print("subscribed")