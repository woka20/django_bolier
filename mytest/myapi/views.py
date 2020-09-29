from django.shortcuts import render
from .models import Hero, Book
from .serializers import AuthorSerializer, BookSerializer, ThirdApiSerializer
from rest_framework import generics
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from Arajaongkir.thirdapi import get_rajaongkir
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import permissions
from myapi.permission import CustomDjangoModelPermissions

# Create your views here.
class AuthorView(generics.ListCreateAPIView):
    queryset=Hero.objects.all().order_by('id')
    serializer_class=AuthorSerializer
    http_method_names=["get","post", "UPDATE","DELETE"]
    permission_classes=[permissions.IsAuthenticated,CustomDjangoModelPermissions]
    


     
class ThirdAPIView(generics.ListCreateAPIView):
    serializer_class= ThirdApiSerializer
    def get(self, request):
        return Response (get_rajaongkir())


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