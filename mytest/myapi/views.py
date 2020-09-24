from django.shortcuts import render
from .models import Hero, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404

# Create your views here.
class AuthorView(generics.ListCreateAPIView):
    queryset=Hero.objects.all().order_by('id')
    serializer_class=AuthorSerializer

class AuthorProfileView(generics.RetrieveAPIView):
    def get(self, request, pk):
        poll = get_object_or_404(Hero, pk=pk)
        data = AuthorSerializer(poll).data
        return Response(data)
 

class BookViewSet(generics.ListCreateAPIView):
    """
    List all workkers, or create a new worker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['release_date']