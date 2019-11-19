from flask import Blueprint, jsonify, request
from models.publishedBook import PublishedBook
from schemas.publishedBook_schema import published_book, published_books
from models.shared_model import db

publishedpublishedBook_controller = Blueprint('publishedBook_controller', __name__)


@publishedpublishedBook_controller.route('/api/publishedBook', methods=['GET'])
def get_publishedBook():
    all_publishedBook = PublishedBook.query.all()
    result = published_books.dump(all_publishedBook)
    return jsonify(result)


@publishedpublishedBook_controller.route('/api/publishedBook', methods=['POST'])
def add_publishedBook():
    user_id = request.json['user_id']
    book_id = request.json['book_id']

    new_publishedBook = PublishedBook(user_id=user_id, book_id=book_id)

    db.session.add(new_publishedBook)
    db.session.commit()

    return published_book.jsonify(new_publishedBook)


@publishedpublishedBook_controller.route('/api/publishedBook/<id>', methods=['PUT'])
def edit_publishedBook(id):
    publishedBook = PublishedBook.query.get(id)

    user_id = request.json['user_id']
    book_id = request.json['book_id']
    dateOfIssue = request.json['dateOfIssue']
    dateOfReturn = request.json['dateOfReturn']

    publishedBook.user_id = user_id
    publishedBook.book_id = book_id
    publishedBook.dateOfIssue = dateOfIssue
    publishedBook.dateOfReturn = dateOfReturn

    db.session.commit()

    return published_book.jsonify(publishedBook)


@publishedpublishedBook_controller.route('/api/publishedBooks/<id>', methods=['DELETE'])
def delete_publishedBook(id):
    publishedBook = PublishedBook.query.get(id)

    db.session.delete(publishedBook)
    db.session.commit()

    return published_book.jsonify(publishedBook)
