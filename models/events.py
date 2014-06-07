from database import db
class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    latitude = db.Column(db.Float(Precision=64), nullable=True)
    longitude = db.Column(db.Float(Precision=64), nullable=True)
