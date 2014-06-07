class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    facebook_id = db.Column(db.Integer, nullable=True)
    profile_pic = db.Column(db.String, nullable=True)