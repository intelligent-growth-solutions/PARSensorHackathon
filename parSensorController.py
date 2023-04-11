import connect
final_readings = []

class ParSensorController():
    def __init__(self):
        return

    def read_on_par(self):
        # print("Reading sensor value")
        # sensor = connect.Quantum()
        # sensor.read_voltage()
        # final_readings.append(sensor.get_micromoles())

        print("Reading sensor value")
        sensor = connect.Quantum()
        sensor.read_voltage()
        print(sensor.read_voltage())
        final_readings.append(sensor.read_voltage())

    def get_final_positions(self):
        return final_readings