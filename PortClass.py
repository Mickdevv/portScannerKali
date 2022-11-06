from pymongo import MongoClient
import ConnectMongoDB

class portClass:
    def __init__(self, hostname, portnumber, protocol, ip):
        self.hostName = hostname
        self.Frequency = 1
        self.portNumber = portnumber
        self.Protocol = protocol
        self.ID = str(self.hostName) + "/" + str(self.portNumber)

        self.updateDB()

        print("ID: " + self.ID + " | Host name : " + str(self.hostName) + " | Port: " + str(self.portNumber) + " | Protocol: " + str(self.Protocol) + " | Frequency: " + str(self.Frequency))

    def getHostName(self):
        return self.hostName

    def setHostName(self, hostname):
        self.hostName = hostname

    def getID(self):
        return self.ID

    def getPortNumber(self):
        return self.portNumber

    def setPortNumber(self, portnumber):
        self.portNumber = portnumber

    def getProtocol(self):
        return self.Protocol

    def setProtocol(self, protocol):
        self.Protocol = protocol

    def getFrequency(self):
        return self.Frequency

    def updateDB(self):
        # cluster = MongoClient(
        #     "mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
        # db = cluster["myDatabase"]
        collection = ConnectMongoDB.connectDB()

        entrySearchResult = collection.find_one({"_id": self.ID})
        if entrySearchResult is None:
            post = {"_id": self.ID, "hostName": self.hostName, "Port": self.portNumber, "protocol": self.Protocol, "Frequency": self.Frequency}
            collection.insert_one(post)
        else:
            collection.update_one({"_id": self.ID}, {"$inc": {"Frequency": 1}})
            self.Frequency = collection.find_one({"_id": self.ID})["Frequency"]