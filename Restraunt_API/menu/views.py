import requests
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Menu
from .serializers import MenuSerializer
# Create your views here.

def Menu_list(request):
    menu = Menu.objects.all()