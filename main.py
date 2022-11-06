import PortScanner
import sys
import BannerRender as br
import pymongo
from pymongo import MongoClient

br.printBanner("Welcome")

# cluster = MongoClient("mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
# db = cluster["myDatabase"]
# collection = db["hof"]
#
# post = {"_id": 80, "Protocol": "http", "Frequency": 0}
#
# collection.insert_one(post)
#
# a = collection.find({"Protocol": "http"})
#
# for result in a:
#     print(result)

PortScanner.portScan(sys.argv[1])
PortScanner.portScan(sys.argv[1])