from models.shared_model import db


# UserBook model

class UserBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    surname_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<UserBook %r>' % self.last_name
