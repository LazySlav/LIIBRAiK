"""
URL configuration for LIIBRAiK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.views import LoginView

from . import views
# from .views import test
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/login/', LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    # path('auth/logout/', views.LogoutView.as_view(), name='logout'),
]
urlpatterns += router.urls
