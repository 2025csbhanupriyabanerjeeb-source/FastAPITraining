#This file cretaes a single, shared connection to MongoDB 
from pymongo import  MongoClient
from pymongo.database import Database

from app.config import settings

#MongoClient manages a poo; of connections to the MongoDB server.
client : MongoClient = MongoClient(settings.MONGO_URI)
database: Database = client[settings.MONGO_DB_NAME]

# Sends a pin
def ping_database() -> bool:
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False