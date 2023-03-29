import connect
import time

def main():
    q = connect.Quantum()

    while True:
        voltage = q.read_voltage()
        print(voltage)
        time.sleep(1)
        
if __name__ == "__main__":
    main()
