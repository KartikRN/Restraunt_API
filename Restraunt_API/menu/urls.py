from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.Menu_list, name ='menu_list'),
    path('menu_item/<str:slug>', views.item_details, name ='menu_item')
]