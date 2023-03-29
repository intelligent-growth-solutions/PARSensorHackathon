import connect

def main():
    q = connect.Quantum()

    while True:
        voltage = q.read_voltage()
        print(voltage)
        
if __name__ == "__main__":
    main()
