from database import db
from categories import *
class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    latitude = db.Column(db.Float(Precision=64), nullable=True)
    longitude = db.Column(db.Float(Precision=64), nullable=True)
    description = db.Column(db.String, nullable=True)
    category_id = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String, nullable=True)
    privacy = db.Column(db.String, nullable=True)
    n_people = db.Column(db.Integer, nullable=True)
    host_name = db.Column(db.Integer, nullable=True)
    tags = db.Column(db.String, nullable=True)

    def to_json(self):
        cat = db.session.query(Category).filter_by(id=self.category_id).all()[0]
        return dict(id=self.id, activity=self.activity, start_time=self.start_time.isoformat(), end_time=self.end_time.isoformat(), latitude=self.latitude, longitude=self.longitude, description=self.description, category=cat.to_json(), address=self.address, privacy=self.privacy, n_people=self.n_people, host_name=self.host_name, tags=self.tags)