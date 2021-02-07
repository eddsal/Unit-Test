
from django.urls import path, include
from main.views import createValidUser
from main.views import index


app_name = "main"

urlpatterns = [
    path('', index),
    path('create/user', createValidUser,name='createValidUser'),

]
