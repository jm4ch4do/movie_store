from rest_framework import serializers
from .models import Author, Book, BookNumber, Character


class BookNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = CharacterSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'characters', 'number', 'authors']


# you can have more than one serializer per Class
class BookMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title']

