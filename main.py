import PortScanner
import socket
import sys
from datetime import datetime

print("Main started...\n")

hostName = sys.argv[1]
print(hostName)
#hostName = "tryhackme.com"
#print(socket.gethostbyname(hostName))
print("Scanning " + hostName + " (" + socket.gethostbyname(hostName) + ") " + " started at : " + str(datetime.now()))
openPorts = []
host = socket.gethostbyname(hostName)
for i in range(10000):
    openPort = PortScanner.portScanner(i, host)
    if openPort != -1:
        openPorts.append(openPort)
        #print(openPorts)

print(openPorts)
