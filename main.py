import connect
from page import Page

def main():
    page = Page()
    page.create_window()

# TODO wire back in
def getVoltage():
    q = connect.Quantum()
    print(q.read_voltage())

if __name__ == "__main__":
    main()


