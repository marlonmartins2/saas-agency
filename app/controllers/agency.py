from database.connection import database
from database.collections import Collections


class Agency:

    @classmethod
    def insert_one(cls, data):
        data["data_criacao"] = data.get("data_criacao").isoformat()
        return database[Collections.AGENCIES].insert_one(data)
    
    @classmethod
    def find_one(cls, arg={}, reject={"_id": 0}):
        return database[Collections.AGENCIES].find_one(arg, reject)
    
    @classmethod
    def find(cls, arg={}, reject={"_id": 0}):
        return database[Collections.AGENCIES].find(arg, reject)
    
    @classmethod
    def update_one(cls, arg, data):
        return database[Collections.AGENCIES].update_one(arg, data, return_document=True)
    
    @classmethod
    def delete_one(cls, arg):
        return database[Collections.AGENCIES].delete_one(arg)
