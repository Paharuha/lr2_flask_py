from flask import Flask, request, jsonify
import os

from models.shared_model import db
from schemas.shared_schema import ma

from controllers.book_controller import book_controller
from controllers.publishedBook_controller import publishedpublishedBook_controller
from controllers.userBook_controller import userBook_controller

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# Data Base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
# db = SQLAlchemy(app)
db.app = app
db.init_app(app)
# Init ma
ma.init_app(app)

# Register routes
app.register_blueprint(book_controller)
app.register_blueprint(publishedpublishedBook_controller)
app.register_blueprint(userBook_controller)

if __name__ == '__main__':
    app.run(debug=True)