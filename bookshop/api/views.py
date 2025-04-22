from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import BookSerializer


@api_view(['POST'])
def create_book(request):
    book_data = JSONParser().parse(request)
    book_serializer = BookSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_user(request):
    pass
