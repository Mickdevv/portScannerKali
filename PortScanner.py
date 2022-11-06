import socket
import BannerRender as br
import ConnectMongoDB
import PortClass
from datetime import datetime


def portScanner(port, host):
    socket.setdefaulttimeout(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((host, port)):
        return -1
    else:
        print("--------- Port " + str(port) + " is open ---------")
        return port

# def generatePortFrequencyList(ip):
#     ports = []
#     collection = ConnectMongoDB()
#     results = collection.find_one({"IP": ip})
#     for result in results:
#         ports.append(result)
#
#     #Bubble sort
#
#
#     return sortedPorts

def portScan(hostname):

    br.printBanner("Port scanner")

    # post = {"name": "Michael", "score": 5}
    # collection.
    # collection.insert_one(post)
    scanStartTime = datetime.now()

    print('Scanning ' + hostname + " (" + socket.gethostbyname(hostname) + "). Started at : " + str(datetime.now()) + "\n")

    openPorts = []
    host = socket.gethostbyname(hostname)
    firstPort = 79
    lastPort = 444
    try:
        for i in range(firstPort, lastPort):
            openPort = portScanner(i, host)

            if openPort != -1:
                #print(openPort)
                #print(socket.getservbyport(openPort) + "\n")
                openPorts.append(PortClass.portClass(openPort, socket.getservbyport(openPort), socket.gethostbyname(hostname)))

        print("\nTotal time taken: " + str(datetime.now() - scanStartTime) + "\n")

        if len(openPorts) == 0:
            print("No open ports found")
        else:
            for port in openPorts:
                print("IP: " + str(port.getIP()) + " | Port: " + str(port.getPortNumber()) + " | Protocol : " + str(port.getProtocol()) + " | Frequency: " + str(port.getFrequency()))

    except KeyboardInterrupt:
        print("\nExiting...")
    except socket.gaierror:
        print("\nHostname could not be resolved")
    except socket.error:
        print("\nServer not responding")
