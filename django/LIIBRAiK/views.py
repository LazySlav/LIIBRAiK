import secrets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
from django.contrib.auth.hashers import Argon2PasswordHasher
from .permissions import *
from rest_framework import request


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def __passwordify(self, request: request.Request):
        request.data._mutable = True
        password = request.data.get('password')
        if not password:
            raise ValueError
        hasher = Argon2PasswordHasher()
        encrypted_password = hasher.encode(password, secrets.token_hex(16))
        request.data['password'] = encrypted_password

    def create(self, request: request.Request, *args, **kwargs):
        try:
            self.__passwordify(request)
        except ValueError:
            return Response({'password': ['This field is required.']},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request: request.Request, *args, **kwargs):
        try:
            self.__passwordify(request)
        except ValueError:
            return Response({'password': ['This field is required.']},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        try:
            self.__passwordify(request)
        except ValueError:
            return Response({'password': ['This field is required.']},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().partial_update(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
