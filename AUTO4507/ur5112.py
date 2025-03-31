# Echo client program
import socket
import time
HOST = "192.168.0.9" # the remote host
PORT = 30002 # The same part used by server
count = 0

while count < 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(0.5)

    s.send("set_digital_out(2,True)"+"\n") # set 2 to high
    time.sleep(0.5)

    # robot moves to positions based on linear
    s.send("movel([-1.95, -1.58, 1.16, -1.15, -1.55, 1.10], a=1.0, v=0.1)"+"\n")
    time.sleep(1)
    # robot moves to positions based on linear
    s.send("movel([-1.95, -1.58, 1.16, -1.15, -1.55, 1.10], a=1.0, v=0.1)"+"\n")
    time.sleep(1)
    # robot moves to positions based on linear
    s.send("movel([-1.95, -1.58, 1.16, -1.15, -1.55, 1.10], a=1.0, v=0.1)"+"\n")
    time.sleep(1)
    # robot moves to positions based on linear
    s.send("movel([-1.95, -1.58, 1.16, -1.15, -1.55, 1.10], a=1.0, v=0.1)"+"\n")
    time.sleep(1)

    count += 1
    data = s.recv(1024)

    s.close()

    print("Received", repr(data))