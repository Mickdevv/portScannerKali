import socket
from datetime import datetime

def portScanner(port, host):
    socket.setdefaulttimeout(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #print("Scanning....")
    if s.connect_ex((host, port)):
        #print("Port " + str(port) + " is closed")
        return -1
    else:
        print("--------- Port " + str(port) + " is open ---------")
        return port


