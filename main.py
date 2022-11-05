from pymongo import MongoClient
import PortScanner
import socket
import sys
import BannerRender as br
from pyfiglet import Figlet
from datetime import datetime
from PortClass import PortClass

br.printBanner("Welcome")

PortScanner.portScan(sys.argv[0])
