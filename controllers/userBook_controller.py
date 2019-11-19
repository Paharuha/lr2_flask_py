from flask import Blueprint, jsonify, request
from models.userBook import UserBook
from schemas.userBook_shema import user_book_schema, user_books_schema
from models.shared_model import db

userBook_controller = Blueprint('userBook_controller', __name__)


@userBook_controller.route('/api/users', methods=['GET'])
def get_user():
    all_users = UserBook.query.all()
    result = user_books_schema.dump(all_users)
    return jsonify(result)


@userBook_controller.route('/api/users', methods=['POST'])
def add_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    surname_name = request.json['surname_name']
    email = request.json['email']
    number = request.json['number']

    new_user = UserBook(first_name=first_name, last_name=last_name, surname_name=surname_name,
                        email=email, number=number)

    db.session.add(new_user)
    db.session.commit()

    return user_book_schema.jsonify(new_user)


@userBook_controller.route('/api/users/<id>', methods=['PUT'])
def edit_user(id):
    user = UserBook.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    surname_name = request.json['surname_name']
    email = request.json['email']
    number = request.json['number']

    user.first_name = first_name
    user.last_name = last_name
    user.surname_name = surname_name
    user.email = email
    user.number = number

    db.session.commit()

    return user_book_schema.jsonify(user)


@userBook_controller.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = UserBook.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_book_schema.jsonify(user)
