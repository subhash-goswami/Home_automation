import os
from flask import Flask
from flask_restful import Api
from resources.relay_resources import Relay, RelayGetAll, RelayGetOne, RelayUpdateOne

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# This is when we used postman
# It is first create our all dbs

# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(Relay, '/relay/<string:rid>/<string:relay_name>/<string:status>')  # Insert, Update, Delete
api.add_resource(RelayGetOne, '/relaygetone/<string:rid>')
api.add_resource(RelayUpdateOne, '/relayupdateone/<string:rid>/<string:status>')
api.add_resource(RelayGetAll, '/gets')

if __name__ == '__main__':
    from db import db  # circular importing
    db.init_app(app)
    app.run(port=8001,debug=True)
