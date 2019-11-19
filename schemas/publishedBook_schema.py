from schemas.shared_schema import ma
from schemas.book_shema import book_schema
from schemas.userBook_shema import user_book_schema
from models.book import Book
from models.userBook import UserBook
from marshmallow import fields


class PublishedBookSchema(ma.ModelSchema):
    idUser = fields.Method('build_user')
    idBook = fields.Method('build_book')

    @staticmethod
    def build_user(obj):
        user = UserBook.query.get(obj.user_id)
        return user_book_schema.dump(user)

    @staticmethod
    def build_book(obj):
        book = Book.query.get(obj.book_id)
        return book_schema.dump(book)

    class Meta:
        fields = ('id', 'user_id', 'book_id', 'dateOfIssue', 'dateOfReturn')


published_book = PublishedBookSchema()
published_books = PublishedBookSchema(many=True)
