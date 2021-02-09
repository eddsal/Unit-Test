
from django.urls import path, include
from main.views import createValidUser, createValidList
from main.views import index


app_name = "main"

urlpatterns = [
    path('', index),
    path('create/user', createValidUser, name='createValidUser'),
    path('create/list', createValidList, name='createValidList'),
    
]
