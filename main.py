import PortScanner
import socket

hostName = "hackthissite.org"
#hostName = "tryhackme.com"

print("Scanning " + hostName + " (" + socket.gethostbyname(hostName) + ") ")

openPorts = []
host = socket.gethostbyname(hostName)
for i in range(10000):
    openPort = PortScanner.portScanner(i, host)
    if openPort != -1:
        openPorts.append(openPort)
        #print(openPorts)

print(openPorts)
