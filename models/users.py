from database import db
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    facebook_id = db.Column(db.Integer, nullable=True)
    profile_pic = db.Column(db.String, nullable=True)

    def to_json(self):
	    return dict(id=self.id, name=self.name, facebook_id=self.facebook_id, profile_pic=self.profile_pic)
