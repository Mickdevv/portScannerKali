import socket
from BannerRender import printBanner as br
from pymongo import MongoClient
import PortClass
from datetime import datetime


def portScanner(port, host):
    socket.setdefaulttimeout(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # print("Scanning....")
    if s.connect_ex((host, port)):
        # print("Port " + str(port) + " is closed")
        return -1
    else:
        print("--------- Port " + str(port) + " is open ---------")
        return port


def portScan(hostname):

    cluster = MongoClient("mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["myDatabase"]
    collection = db["hof"]

    # post = {"name": "Michael", "score": 5}
    # collection.
    # collection.insert_one(post)

    br.printBanner("Port scanner")

    print("Scanning " + hostname + " (" + socket.gethostbyname(hostname) + ") " + " started at : " + str(
        datetime.now()) + "\n")

    openPorts = []
    host = socket.gethostbyname(hostname)
    try:
        for i in range(79, 444):
            openPort = portScanner(i, host)
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

    except KeyboardInterrupt:
        print("\nExiting...")
    except socket.gaierror:
        print("\nHostname could not be resolved")
    except socket.error:
        print("\nServer not responding")
