import PortScanner
import socket
import sys
from datetime import datetime

print("Main started...\n")

hostName = sys.argv[1]

print("Scanning " + hostName + " (" + socket.gethostbyname(hostName) + ") " + " started at : " + str(datetime.now()) + "\n")

openPorts = []
host = socket.gethostbyname(hostName)
for i in range(79,500):
    openPort = PortScanner.portScanner(i, host)
    if openPort != -1:
        openPortTemp = []
        openPortTemp.append(openPort)
        openPortTemp.append(socket.getservbyport(openPort))
        openPorts.append(openPortTemp)
        print(socket.getservbyport(openPort))
        #print(openPorts)

print(openPorts)
