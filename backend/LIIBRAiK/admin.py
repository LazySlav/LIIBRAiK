from django.contrib import admin
from .models import *

models = [User, Author, Publisher, Book, Reservation]
admin.site.register(models)
