from schemas.shared_schema import ma


class UserBookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'surname_name', 'email', 'number')


user_book_schema = UserBookSchema()
user_books_schema = UserBookSchema(many=True)
