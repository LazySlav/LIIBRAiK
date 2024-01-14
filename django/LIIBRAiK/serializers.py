from rest_framework import serializers
from .models import User, Author, Publisher, Book, BookToAuthor, Reservation
from django.contrib.auth.hashers import Argon2PasswordHasher
import secrets

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
                  'last_name', 'mail', 'last_login', 'role', 'is_active', 'password']

    def __passwordify(self, validated_data):
        plain_password = validated_data['password']
        hasher = Argon2PasswordHasher()
        encrypted_password = hasher.encode(
            plain_password, secrets.token_hex(16))
        return encrypted_password

    def create(self, validated_data):
        self.__passwordify(validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance: User, validated_data):
        self.__passwordify(validated_data)
        return super().update(instance, validated_data)
