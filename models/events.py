from database import db
class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    latitude = db.Column(db.Float(Precision=64), nullable=True)
    longitude = db.Column(db.Float(Precision=64), nullable=True)
    description = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    privacy = db.Column(db.String, nullable=True)
    n_people = db.Column(db.Integer, nullable=True)
    host_id = db.Column(db.Integer, nullable=True)
    tags = db.Column(db.String, nullable=True)
