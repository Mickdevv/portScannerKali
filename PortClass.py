from pymongo import MongoClient
import ConnectMongoDB

class portClass:
    def __init__(self, hostname, portnumber, protocol, ip):
        self.hostName = hostname
        self.Frequency = 1
        self.portNumber = portnumber
        self.Protocol = protocol
        self.ID = str(self.hostName) + "/" + str(self.portNumber)

        #Adds the entry to the database
        self.updateDB()

        #print("ID: " + self.ID + " | Host name : " + str(self.hostName) + " | Port: " + str(self.portNumber) + " | Protocol: " + str(self.Protocol) + " | Frequency: " + str(self.Frequency))

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
        #Connect to the mongodb database
        collection = ConnectMongoDB.connectDB()

        # Query the database to check for this entry's existence
        entrySearchResult = collection.find_one({"_id": self.ID})

        # If the entry does not exist, create a new one
        if entrySearchResult is None:
            post = {"_id": self.ID, "hostName": self.hostName, "Port": self.portNumber, "protocol": self.Protocol, "Frequency": self.Frequency}
            collection.insert_one(post)
        # If the entry exists, update it
        else:
            collection.update_one({"_id": self.ID}, {"$inc": {"Frequency": 1}})
            self.Frequency = collection.find_one({"_id": self.ID})["Frequency"]