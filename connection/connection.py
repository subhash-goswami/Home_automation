from pymongo import MongoClient


class ConnectionModel:
    @staticmethod
    def connect():
        con_url=MongoClient("mongodb://admin:admin123@localhost:27017/")
        return con_url["home_automation"]["relay_status"]
