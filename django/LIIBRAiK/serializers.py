from rest_framework import serializers
from .models import User, Author, Publisher, Book, BookToAuthor, Reservation


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['publisher_id', 'name']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['book_id', 'name', 'year', 'ISBN', 'authors',
                  'publisher', 'description', 'amounts', 'cover', 'pdf']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservation_id', 'user', 'book',
                  'start_date', 'end_date', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'library_card', 'name', 'surname',
                  'last_name', 'mail', 'last_login', 'role', 'is_active']
