#Mapping urls to views
from django.urls import path
from . import views

urlpatterns =[
    path('index/',views.index),
    path('inventory/', views.inventory),
    path('admin/', views.admin)
]