from schemas.shared_schema import ma


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nameBook', 'avtor', 'kindOf', 'year', 'code')


book_schema = BookSchema()
books_schema = BookSchema(many=True)
