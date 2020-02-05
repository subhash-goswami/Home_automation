from connection.connection import ConnectionModel
from flask_restful import Resource


class Relay(Resource):
    mongo_client = ConnectionModel.connect()

    def post(self, rid, relay_name, status):
        try:
            result = self.mongo_client.insert_one(
                {"_id": int(rid), "relay_name": relay_name, "status": int(status)})
            if result:
                return {"message": "New relay is Added successfully",
                        "relay id": result.inserted_id}, 201  # Created new Relay
        except Exception as e:
            return {"ERROR": "While inserting Relay details: " + str(e)}, 400  # Bad Request

    def get(self, rid, relay_name, status):
        try:
            result = self.mongo_client.find_one({"_id": int(rid)})
            if result:
                return {"Relay details": result}, 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While fetching relay details :" + str(e)}

    def put(self, rid, relay_name, status):
        try:
            result = self.mongo_client.find_one_and_update({"_id": int(rid)},
                                                           {"$set": {"relay_name": relay_name,
                                                                     "status": int(status)}})
            if result:
                return {"message": "Data is updated successfully", "Old data": result}, 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While updating relay details :" + str(e)}

    def delete(self, rid, relay_name, status):
        try:
            result = self.mongo_client.find_one_and_delete({"_id": int(rid), "relay_name": relay_name})
            if result:
                return {"message": "Data is deleted successfully", "Old data": result}, 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While deleting relay details :" + str(e)}


class RelayGetOne(Resource):
    mongo_client = ConnectionModel.connect()

    def get(self, rid):
        try:
            result = self.mongo_client.find_one({"_id": int(rid)})
            if result:
                return result['status'], 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While fetching relay details: " + str(e)}


class RelayUpdateOne(Resource):
    mongo_client = ConnectionModel.connect()

    def put(self, rid,status):
        try:
            result = self.mongo_client.find_one_and_update({"_id": int(rid)}, {"$set": {"status": int(status)}})
            if result:
                return {"message": "status is updated","Old Data":result}, 200
        except Exception as e:
            return {"ERROR": "While fetching relay details :" + str(e)}


class RelayGetAll(Resource):
    mongo_client = ConnectionModel.connect()

    def get(self):
        try:
            result = self.mongo_client.find()
            if result.count() > 0:
                return {"Relay Details": [r for r in result]}, 200  # OK
            return {"message": "No Relay is available in Database"}, 404
        except Exception as e:
            return {"ERROR": "while getting all relay details: " + str(e)}, 400  # Bad Request
