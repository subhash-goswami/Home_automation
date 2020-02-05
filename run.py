from app import app
from db import db

db.init_app(app)  # it is first initalize app this is run first run.py and than app.py files

@app.before_first_request
def create_tables():
    db.create_all()