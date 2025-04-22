from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST',])
def home(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    if request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
