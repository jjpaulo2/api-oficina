from pymongo import MongoClient
from pymongo.database import Database

__DATABASE_NAME = 'oficina'
__DATABASE_HOST = 'localhost'
__DATABASE_PORT = 27017

__client = MongoClient(__DATABASE_HOST, __DATABASE_PORT)

def database() -> Database:
    return __client[__DATABASE_NAME]