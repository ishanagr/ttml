from database import db
class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)

    def to_json(self):
	    return dict(id=self.id, title=self.title, image=self.image)
