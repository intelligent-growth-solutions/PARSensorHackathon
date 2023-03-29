import connect
from page import Page

def main():
    page = Page()
    page.create_window()

    q = connect.Quantum()

    while True:
        voltage = q.read_voltage()
        print(voltage)
        
if __name__ == "__main__":
    main()
