import connect

def main():
    q = connect.Quantum()
    print(q.read_voltage())
    return

if __name__ == "__main__":
    main()
