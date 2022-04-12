from rest_framework import serializers
from .models import Book, BookNumber


class BookNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price']

