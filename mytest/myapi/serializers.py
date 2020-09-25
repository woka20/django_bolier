from rest_framework import serializers
from .models import Hero, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model=Hero
        fields=('id','name','alias')

class ThirdApiSerializer(serializers.Serializer):
        mapped_object=[]
      

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Book
        fields = ("id", "title", "description", "publisher", "release_date")
        extra_kwargs = {'authors': {'required': False}}