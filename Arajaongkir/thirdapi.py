from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from myapi.serializers import ThirdApiSerializer
import requests

def get_rajaongkir():
    responses= requests.get('https://api.rajaongkir.com/starter/city', params={'key':'fb63156a683784f4edbd8f23ea73a4a3'})
    geodata = responses.json()
    return geodata