from models.shared_model import db
from datetime import datetime


# PublishedBook model
class PublishedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_book.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    dateOfIssue = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    dateOfReturn = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return '<PublishedBook %r>' % self.id