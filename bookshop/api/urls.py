from django.urls import path
from .views import register_user, create_book

urlpatterns = [
    path('', create_book, name='api-create_book'),
    path('registration', register_user, name='api-register'),
]