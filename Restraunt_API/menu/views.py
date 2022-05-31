import requests
from rest_framework.parsers import FormParser,MultiPartParser
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Menu
from .serializers import MenuSerializer
# Create your views here.

@api_view(['GET','POST'])
def Menu_list(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        parser_classes = [MultiPartParser, FormParser]
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def item_details(request,slug):
    try:
        item = Menu.objects.get(Item_name = slug)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MenuSerializer(item)
    return Response(serializer.data)