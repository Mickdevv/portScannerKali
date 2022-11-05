import pyfiglet
import pymongo
from pymongo import MongoClient
import PortScanner
import socket
import sys
from pyfiglet import Figlet
from datetime import datetime
from PortClass import PortClass


def portScan():
    cluster = MongoClient("mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["myDatabase"]
    collection = db["hof"]

    # post = {"name": "Michael", "score": 5}
    # collection.
    # collection.insert_one(post)

    fonts = ['roman', 'doh', 'banner4', 'char3___', 'banner3', 'clb8x10', 'colossal', 'univers', 'starwars']


    # Print banner
    f = Figlet(font=fonts[-2])
    print(f.renderText('Scanner started'))

    hostName = sys.argv[1]

    print("Scanning " + hostName + " (" + socket.gethostbyname(hostName) + ") " + " started at : " + str(
        datetime.now()) + "\n")

    openPorts = []
    host = socket.gethostbyname(hostName)
    for i in range(79, 444):
        openPort = PortScanner.portScanner(i, host)
        if openPort != -1:
            openPortTemp = []
            openPorts.append(PortClass(openPort, socket.getservbyport(openPort)))
            # openPortTemp.append(openPort)
            # openPortTemp.append(socket.getservbyport(openPort))
            # openPorts.append(openPortTemp)
            print(socket.getservbyport(openPort))
            # print(openPorts)
    print()
    for port in openPorts:
        print("Port " + str(port.getPortNumber()) + " is open. Protocol : " + str(port.getProtocol()))
    # print(openPorts)

portScan()
