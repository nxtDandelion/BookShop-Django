from rest_framework import serializers
from .models import Book, MyUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description',
                  'authors', 'page_count', 'cover_type',
                  'price', 'publication_date', 'code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'last_login', 'login',
                  'email', 'password', 'birth_date')
