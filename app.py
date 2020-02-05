from flask import Flask
from flask_restful import Resource,Api
from resources.relay_resources import Relay, RelayGetAll, RelayGetOne, RelayUpdateOne

app = Flask(__name__)

api=Api(app)

api.add_resource(Relay, '/relay/<string:rid>/<string:relay_name>/<string:status>')
api.add_resource(RelayGetOne, '/relaygetone/<string:rid>')
api.add_resource(RelayUpdateOne, '/relayupdateone/<string:rid>/<string:status>')
api.add_resource(RelayGetAll, '/gets')

if __name__ == '__main__':
    app.run(port=8001,debug=True)
