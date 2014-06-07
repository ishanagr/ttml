from database import db
class Attend(db.Model):

    __tablename__ = 'attends'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
