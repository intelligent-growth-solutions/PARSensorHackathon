import multiprocessing
import csv
import paho.mqtt.client as mqtt
from parSensorController import ParSensorController

position_index = 0
positions = []
xSteps = 0
ySteps = 0

class MqttController():
    def __init__(self):
        return

    def initialise(self, blockWidth, blockHeight, noXSteps, noYSteps):
        global positions
        global xSteps
        global ySteps
        xSteps = int(noXSteps)
        ySteps = int(noYSteps)
        self.createPositions(blockWidth, blockHeight, noXSteps, noYSteps)

        client = mqtt.Client(client_id="onpar", protocol=mqtt.MQTTv311)

        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_connect = on_connect

        client.username_pw_set(username="igstest", password="testigs18")
        client.connect(host="51.141.82.199", port=1883)

        self.go_to_next_position()

        client.loop_forever()

    def createPositions(self, xLen, yLen, xSteps, ySteps):
        global positions

        block_width = int(xLen) / int(xSteps)
        block_height = int(yLen) / int(ySteps)

        for x in range(int(xSteps)):
            for y in range(int(ySteps)):
                pos_x = x * int(block_width) + (int(block_width) / 2)
                pos_y = y * int(block_height) + (int(block_height) / 2)

                posTuple = (pos_x, pos_y)

                positions.append(posTuple)



    def go_to_next_position(self):
            global position_index

            # send desired position
            print("Sending to position: ", positions[position_index])
            # client.publish("cmd/plc/onpar/position", '{{"X":{},"Y":{}}}'.format(pos_x, pos_y), qos=1)
            # client.publish("cmd/plc/onpar/position", '{{"X":{},"Y":{}}}'.format(pos_x, pos_y), qos=1)

            position_index += 1

def on_connect(client, userdata, flags, rc):
        print("Device connected with result code: " + str(rc))
        client.subscribe("dt/plc/onpar/inposition", qos=0)


def on_disconnect(client, userdata, rc):
        print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
        return

def on_message(client, userdata, message):

        global killThread
        print("Received event: ", message.payload)
        if "TRUE" not in str(message.payload):
            return

        parControl = ParSensorController()
        parControl.read_on_par()

        # THIS IS WHEN WE RETURN
        if position_index == xSteps*ySteps:
            # open the file in the write mode
            with open('results.csv', 'w', newline='') as f:
                # create the csv writer
                writer = csv.writer(f)

                for i in range(position_index):
                    finalReadings = parControl.get_final_positions()
                    #🤮
                    writeVal = (positions[i][0],positions[i][1], finalReadings[i])

                    writer.writerow(writeVal)

            process = multiprocessing.current_process()
            process.terminate()



        MqttController.go_to_next_position(client)

def on_subscribe(client, userdata, mid, qos):
        print("subscribed")
