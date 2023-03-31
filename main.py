import connect
import time
from page import Page
import paho.mqtt.client as mqtt

block_width = 500 / 5
block_height = 800 / 5

do_next_reading = False
x_positions = []
y_positions = []

position_index: int = 0

final_readings = []

def create_positions():
    for x in range(5):
        for y in range(5):
            # calculate position
            pos_x = x * block_width + (block_width / 2)
            pos_y = y * block_height + (block_height / 2)

            x_positions.append(pos_x)
            y_positions.append(pos_y)

def go_to_next_position(client):
    global position_index
    pos_x = x_positions[position_index]
    pos_y = y_positions[position_index]

    # send desired position
    print("Sending to position: ", pos_x, pos_y)
    client.publish("cmd/plc/onpar/position", f'{{"X":{pos_x},"Y":{pos_y}}}', qos=1)

    position_index += 1


def main():
    client = mqtt.Client(client_id="onpar", protocol=mqtt.MQTTv311)

    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect

    client.username_pw_set(username="igstest", password="testigs18")
    client.connect(host="51.141.82.199", port=1883)

    create_positions()
    position_index = 0

    if position_index == 24:
        page = Page()
        page.create_window(final_readings)

    go_to_next_position(client)

    client.loop_forever()

    # UI
    # page = Page()
    # page.create_window()


def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))
    client.subscribe("dt/plc/onpar/inposition", qos=0)


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    return


def on_message(client, userdata, message):
    print("Received event: ", message.payload)
    if "TRUE" not in str(message.payload):
        return
    # read sensor value
    print("Reading sensor value")
    sensor = connect.Quantum()
    reading = sensor.read_voltage()
    # update reading array
    print(reading)
    final_readings.append(reading)
    # got to next position
    go_to_next_position(client)


def on_subscribe(client, userdata, mid, qos):
    print("subscribed")

if __name__ == "__main__":
    main()