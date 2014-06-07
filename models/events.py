from database import db
from marshmallow import Serializer, fields
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

class EventSerializer(Serializer):
    formatted_name = fields.Method("format_name")

    def format_name(self, event):
        return "%s, %s" % (event.id, event.activity, event.start_time, event.end_time, event.latitude, event.longitude, event.description, event.category_id, event.address, event.privacy, event.n_people, event.host_name, event.tags)

    class Meta:
        fields = ('id', 'activity', 'start_time', "end_time", "latitude", "longitude", "description", "category_id", "address", "privacy", "n_people", "host_name", "tags")