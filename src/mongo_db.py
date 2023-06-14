from pymongo import MongoClient
import pandas as pd

def insert_into_mongodb(payload, db_name, collection_name):
    mongoClient = MongoClient()
    db = mongoClient[db_name]
    collection = db[collection_name]
    if isinstance(payload, pd.DataFrame):
        payload = payload.to_dict(orient='records')
    collection.insert_many(payload)