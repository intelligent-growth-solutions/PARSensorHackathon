import multiprocessing
import csv
import sys

import paho.mqtt.client as mqtt
from parSensorController import ParSensorController

position_index = 0
positions = []
outputArray = []
xSteps = 0
ySteps = 0

class MqttController():
    def __init__(self):
        return

    def initialise(self, blockWidth, blockHeight, noXSteps, noYSteps, curSegment):
        global positions
        global xSteps
        global ySteps
        global segment
        xSteps = int(noXSteps)
        ySteps = int(noYSteps)
        segment = curSegment
        self.createPositions(blockWidth, blockHeight, noXSteps, noYSteps)

        client = mqtt.Client(client_id="onpar", protocol=mqtt.MQTTv311)

        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_connect = on_connect

        client.username_pw_set(username="igstest", password="testigs18")
        client.connect(host="51.141.82.199", port=1883)

        go_to_next_position(client)

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



def go_to_next_position(client):
            global position_index

            pos_x = positions[position_index][0]
            pos_y = positions[position_index][1]

            # send desired position
            print("Sending to position: ({}, {})".format(pos_x, pos_y))
            print("Position Index: ", position_index)

            client.publish("cmd/plc/onpar/position", '{{"X":{},"Y":{}}}'.format(pos_x, pos_y), qos=1)

def on_connect(client, userdata, flags, rc):
        print("Device connected with result code: " + str(rc))
        client.subscribe("dt/plc/onpar/inposition", qos=0)


def on_disconnect(client, userdata, rc):
        print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
        return

def error_path():
    print("Error")
    sys.exit()
def on_message(client, userdata, message):
        global position_index
        global segment


        print("Received event: ", message.payload)

        if "ERROR" in str(message.payload):
            error_path()


        if "TRUE" not in str(message.payload):
            return

        parControl = ParSensorController()
        val = parControl.read_on_par()

        #clever way to determine the theoretical coordinate using an incrementing counter

        x = position_index / 3
        y = position_index % 3

        # disgusting🤮
        segmentMap = {
            1: (0, 0),
            2: (3, 0),
            3: (6, 0),
            4: (9, 0),
            5: (12, 0),
            6: (15, 0),
            7: (16, 0),
            8: (16, 6),
            9: (15, 6),
            10: (12, 6),
            11: (9, 6),
            12: (6, 6),
            13: (3, 6),
            14: (0, 6)
        }

        x = x + segmentMap[int(segment)][1]
        y = y + segmentMap[int(segment)][0]

        print(position_index)
        print([int(x), y, val])
        outputArray.append([int(x), y, val])


        # THIS IS WHEN WE RETURN
        if position_index+1 == xSteps*ySteps:
            # open the file in the write mode
            try:
                with open('segments/results{}.csv'.format(segment), 'x', newline='') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    writer.writerows(outputArray)
            except FileExistsError:
                with open('segments/results{}.csv'.format(segment), 'w', newline='') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    writer.writerows(outputArray)

            # process = multiprocessing.current_process()
            # process.terminate()
            sys.exit()

        position_index += 1
        go_to_next_position(client)

def on_subscribe(client, userdata, mid, qos):
        print("subscribed")
