import secrets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
from django.contrib.auth.hashers import Argon2PasswordHasher
from rest_framework import request
from rest_framework.decorators import action



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]
    
    @action(detail=False, methods=['get'])
    def book_search(self, request):
        request.data
        filtered_books = Book.objects.filter().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]
