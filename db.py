import pymongo
import os


mongodb_password=os.getenv("MONGODB_PASSWORD")
connectionURL1=os.getenv("connectionURL1")
connectionURL2=os.getenv("connectionURL2")

def initialiseMongoClient(connectionURL1,mongodb_password,connectionURL2):
    connectURL=connectionURL1+mongodb_password+connectionURL2
    client = pymongo.MongoClient(connectURL)
    return client
