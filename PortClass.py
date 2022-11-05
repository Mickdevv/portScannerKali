class portClass:
    def __init__(self, portnumber, protocol):
        self.portNumber = portnumber
        self.Protocol = protocol

    def getPortNumber(self):
        return self.portNumber

    def setPortNumber(self, portnumber):
        self.portNumber = portnumber

    def getProtocol(self):
        return self.Protocol

    def setProtocol(self, protocol):
        self.portNumber = protocol
