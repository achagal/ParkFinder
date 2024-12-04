import os
import pymongo
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['parkingspaces']
collection = db['spaces']
collection.insert_one(
    {"spaceID": "3272", 
     "location": "Ross",
       "coordinates": (37.234,-98.2234)}
    )
