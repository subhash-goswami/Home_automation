from model.relay_model import RelayModel
from flask_restful import Resource


class Relay(Resource):

    def post(self, rid, relay_name, status):
        try:
            if RelayModel.find_by_relayname(relay_name):
                return {"message": "This relay is already exists"}
            relay = RelayModel(rid=rid, relay_name=relay_name, status=status)
            relay.save_to_db()
            return {"message": "New relay is Added successfully",
                        "relay id": relay.rid}, 201  # Created new Relay
        except Exception as e:
            return {"ERROR": "While inserting Relay details: " + str(e)}, 400  # Bad Request

    def get(self, rid, relay_name, status):
        try:
            relay= RelayModel.find_by_id(rid=rid)
            if relay:
                return {"Relay details": relay.json()}, 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While fetching relay details :" + str(e)}

    def put(self, rid, relay_name, status):
        try:
            relay = RelayModel.find_by_id(rid=rid)
            if relay is None:
                relay = RelayModel(rid=rid, relay_name=relay_name, status=status)
            else:
                relay.relay_name = relay_name
                relay.status = status
            relay.save_to_db()
            return {"message": "Data is updated successfully", "New data": relay.json()}, 200
        except Exception as e:
            return {"ERROR": "While updating relay details :" + str(e)}

    def delete(self, rid, relay_name, status):
        try:
            relay = RelayModel.find_by_id(rid=rid)
            if relay:
                relay.delete_from_db()
                return {"message": "Data is deleted successfully"}, 200
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While deleting relay details :" + str(e)}


class RelayGetOne(Resource):
    def get(self, rid):
        try:
            relay = RelayModel.find_by_id(rid=rid)
            if relay:
                realy_details=relay.json()
                return realy_details['status']
            return {"message": "Data is not found"}, 404
        except Exception as e:
            return {"ERROR": "While fetching relay details :" + str(e)}


class RelayUpdateOne(Resource):

    def put(self, rid, status):
        try:
            relay = RelayModel.find_by_id(rid=rid)
            if relay:
                relay.status = status
            relay.save_to_db()
            return {"message": "Data is updated successfully", "New data": relay.json()}, 200
        except Exception as e:
            return {"ERROR": "While updating relay details :" + str(e)}


class RelayGetAll(Resource):
    def get(self):
        try:
            relay_details=[relay.json() for relay in RelayModel.query.all()]
            if len(relay_details) > 0:
                return {"Relay Details": relay_details}
            return {"message": "No Relay is available in Database"}, 404
        except Exception as e:
            return {"ERROR": "while getting all relay details: " + str(e)}, 400  # Bad Request
