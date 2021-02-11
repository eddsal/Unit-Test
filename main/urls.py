
from django.urls import path, include
from main.views import index, createValidUser, createValidList, getValidList, getValidListItems

app_name = "main"

urlpatterns = [
    path('', index),
    path('user/add', createValidUser, name='createValidUser'),
    path('user/add/list', createValidList, name='createValidList'),
    path('user/add/list/item', createValidList, name='createValidList'),

    path('user/<int:user_id>/get/list', getValidList, name='getValidList'),
    # path('user/<int:user_id>/get/list/items/', getValidListItems, name='getValidListItems'),

    
]
