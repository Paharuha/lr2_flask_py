from flask import Blueprint, jsonify, request
from models.book import Book
from schemas.book_shema import book_schema, books_schema
from models.shared_model import db

book_controller = Blueprint('book_controller', __name__)


@book_controller.route('/api/book', methods=['GET'])
def get_book():
    all_book = Book.query.all()
    result = books_schema.dump(all_book)
    return jsonify(result)


@book_controller.route('/api/book', methods=['POST'])
def add_book():
    nameBook = request.json['nameBook']
    avtor = request.json['avtor']
    genre = request.json['genre']
    kindOf = request.json['kindOf']
    year = request.json['year']
    code = request.json['cade']

    new_book = Book(nameBook=nameBook, avtor=avtor, genre=genre,
                    kindOf=kindOf, year=year, code=code)

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)


@book_controller.route('/api/book/<id>', methods=['PUT'])
def edit_book(id):
    book = Book.query.get(id)

    nameBook = request.json['nameBook']
    avtor = request.json['avtor']
    genre = request.json['genre']
    kindOf = request.json['kindOf']
    year = request.json['year']
    code = request.json['cade']

    book.nameBook = nameBook
    book.avtor = avtor
    book.genre = genre
    book.kindOf = kindOf
    book.year = year
    book.code = code

    db.session.commit()

    return book_schema.jsonify(book)


@book_controller.route('/api/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)

    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)
