import socket
import sys
import time
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid argument amount")

openPorts = []

print("-"*50)
print("Scanning target : " + target)
print("Scanning started at " + str(datetime.now()))
print("-"*50)

try:
    for port in range(1,10000):
        #print(int(((port/65535)*100)), end = "\r")
        print(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)

        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            openPorts.append(port)
        s.close()
    # print("Done")
    if len(openPorts) == 0:
        print("No open ports")
    else:
        print(openPorts)

except KeyboardInterrupt:
    print("\nExiting...")
except socket.gaierror:
    print("\nHostname could not be resolved")
except socket.error:
    print("\nServer not responding")