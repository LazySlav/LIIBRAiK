from django.contrib import admin
from .models import *

models = [User]
admin.site.register(models)
