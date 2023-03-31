import connect
from page import Page
import paho.mqtt.client as mqtt


class Sensor:
    def __init__(self):
        self.block_width = 500 / 5
        self.block_height = 800 / 5

        self.do_next_reading = False
        self.x_positions = []
        self.y_positions = []

        self.position_index: int = 0

        self.final_readings = []

    def take_readings(self):
        client = mqtt.Client(client_id="onpar", protocol=mqtt.MQTTv311)
        self.setup_client(client)

        self.create_positions()
        self.position_index = 0

        # Loop until 25 readings
        if self.position_index == 24:
            page = Page()
            page.create_window(self.final_readings)

        self.go_to_next_position(client)
        client.loop_forever()

    def setup_client(self, client):
        client.on_disconnect = self.on_disconnect
        client.on_publish = self.on_publish
        client.on_message = self.on_message
        client.on_subscribe = self.on_subscribe
        client.on_connect = self.on_connect

        client.username_pw_set(username="igstest", password="testigs18")
        client.connect(host="51.141.82.199", port=1883)

    def create_positions(self):
        for x in range(5):
            for y in range(5):
                # calculate position
                pos_x = x * self.block_width + (self.block_width / 2)
                pos_y = y * self.block_height + (self.block_height / 2)

                self.x_positions.append(pos_x)
                self.y_positions.append(pos_y)

    def go_to_next_position(self, client):
        pos_x = self.x_positions[self.position_index]
        pos_y = self.y_positions[self.position_index]

        # send desired position
        print("Sending to position: ", pos_x, pos_y)
        client.publish("cmd/plc/onpar/position", f'{{"X":{pos_x},"Y":{pos_y}}}', qos=1)

        self.position_index += 1

    def on_connect(self, client, userdata, flags, rc):
        print("Device connected with result code: " + str(rc))
        client.subscribe("dt/plc/onpar/inposition", qos=0)

    def on_disconnect(self, client, userdata, rc):
        print("Device disconnected with result code: " + str(rc))

    def on_publish(self, client, userdata, mid):
        return

    def on_message(self, client, userdata, message):
        print("Received event: ", message.payload)
        if "TRUE" not in str(message.payload):
            return

        # read sensor value
        print("Reading sensor value")
        sensor = connect.Quantum()
        reading = sensor.read_voltage()

        # update reading array
        print(reading)
        self.final_readings.append(reading)
        # got to next position
        self.go_to_next_position(client)

    def on_subscribe(self, client, userdata, mid, qos):
        print("subscribed")