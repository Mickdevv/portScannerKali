from pymongo import MongoClient


def connectDB():
    cluster = MongoClient(
        "mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["myDatabase"]
    collection = db["hof"]

    return collection
