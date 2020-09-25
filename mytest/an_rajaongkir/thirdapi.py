from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from myapi.serializers import ThirdApiSerializer
import requests

class ThirdAPIView(generics.ListCreateAPIView):
    serializer_class= ThirdApiSerializer
    def get(self, request):
        responses= requests.get('https://api.rajaongkir.com/starter/city', params={'key':'<input your own API key>'})
        geodata = responses.json()
        return Response(geodata)