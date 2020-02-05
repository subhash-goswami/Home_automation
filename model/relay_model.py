from db import db

class RelayModel(db.Model):
    __tablename__ = 'home_automation'

    rid = db.Column(db.Integer, primary_key=True)
    relay_name = db.Column(db.String(20))
    status = db.Column(db.Integer)

    def __init__(self, rid, relay_name, status):
        self.rid=rid
        self.relay_name=relay_name
        self.status=status

    def json(self):
        return {'id':self.rid, "relay_name": self.relay_name, "status":self.status}

    @classmethod
    def find_by_id(cls,rid):
        return cls.query.filter_by(rid=rid).first()

    @classmethod
    def find_by_relayname(cls, relay_name):
        return cls.query.filter_by(relay_name=relay_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()