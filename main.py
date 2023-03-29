import connect

def main():
    o: object
    q = connect.Quantum(o)
    print(q.read_voltage())
    return

if __name__ == "__main__":
    main()