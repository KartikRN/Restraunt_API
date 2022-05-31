import requests
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
        return JsonResponse({'menu':serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)