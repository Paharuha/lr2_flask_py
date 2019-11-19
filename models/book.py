from models.shared_model import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameBook = db.Column(db.String(20), nullable=False)
    avtor = db.Column(db.String(20), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    kindOf = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.nameBook
