import pymongo
import certifi
from dotenv import load_dotenv
import os
 
load_dotenv('odm_server.env') 

CONNECTION_STR = os.environ.get("CONNECTION_STR")

client = pymongo.MongoClient(CONNECTION_STR , serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())
db = client.myFirstDatabase
usersCollection = db.users


