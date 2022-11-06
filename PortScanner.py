import socket
import time
import BannerRender as br
import ConnectMongoDB
import PortClass
from datetime import datetime
from tqdm import tqdm


def portScannerLoop(firstPort, lastPort, host, hostname, frequentPorts, openPorts):
    try:
        for j in tqdm(range(firstPort, lastPort)):
            openPort = portScanner(j, host)

            if openPort != -1:
                present = False
                for port in frequentPorts:
                    if j == port[0]:
                        present = True
                    if not present:
                        print("--------- Port " + str(openPort) + " is open ---------")
                        openPorts.append(PortClass.portClass(hostname, openPort, socket.getservbyport(openPort), host))


    except KeyboardInterrupt:
        print("\nExiting...")
    except socket.gaierror:
        print("\nHostname could not be resolved")
    except socket.error:
        print("\nServer not responding")

    return openPorts


def portScannerList(frequentPorts, host, hostname, openPorts, firstPort, lastPort):
    try:
        for port in frequentPorts:
            openPort = portScanner(port[0], host)

            if openPort != -1 and firstPort <= openPort <= lastPort:
                print("--------- Port " + str(openPort) + " is open ---------")
                openPorts.append(PortClass.portClass(hostname, openPort, socket.getservbyport(openPort), host))

    except KeyboardInterrupt:
        print("\nExiting...")
    except socket.gaierror:
        print("\nHostname could not be resolved")
    except socket.error:
        print("\nServer not responding")

    return openPorts


def portScanner(port, host):
    socket.setdefaulttimeout(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((host, port)):
        return -1
    else:
        return port


def generatePortFrequencyList(host):
    ports = []
    collection = ConnectMongoDB.connectDB()
    results = collection.find({"hostName": host})
    for result in results:
        # print(result)
        ports.append([result["Port"], result["Frequency"]])

    # print("Before")
    # print(ports)

    # Bubble sort
    for i in range(len(ports)):
        for j in range(len(ports) - 1):
            if ports[j][1] < ports[j + 1][1]:
                temp = ports[j]
                ports[j] = ports[j + 1]
                ports[j + 1] = temp
    # print("After")
    # print(ports)

    return ports


def portScanMain(hostname, iterations):
    br.printBanner("Port scanner")

    scanStartTime = datetime.now()

    host = socket.gethostbyname(hostname)
    print('Scanning ' + hostname + " (" + host + "). Started at : " + str(
        datetime.now()) + "\n")

    for i in range(iterations):

        firstPort = 79
        lastPort = 444

        # initialisation of openPorts list
        openPorts = []

        # Show start time
        print("\n--- Iteration " + str(i + 1) + "/" + str(iterations) + " ---\n")

        # Generate a list of the most frequently open ports for this hostName by querying the database
        frequentPorts = generatePortFrequencyList(hostname)

        if len(frequentPorts) != 0:
            # Scan the most frequently open ports from the list
            openPorts = portScannerList(frequentPorts, host, hostname, openPorts, firstPort, lastPort)

        openPorts = portScannerLoop(firstPort, lastPort, host, hostname, frequentPorts, openPorts)

        if len(openPorts) == 0:
            print("No open ports found")
        else:
            for port in openPorts:
                print("ID: " + str(port.getID()) + " | Port: " + str(port.getPortNumber()) + " | Protocol : " + str(
                    port.getProtocol()) + " | Frequency: " + str(port.getFrequency()))

        print("\nTotal time taken: " + str(datetime.now() - scanStartTime) + "\n")
