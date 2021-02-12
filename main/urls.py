
from django.urls import path, include
from main.views import index, createValidUser, createValidList,createValidListItem, getValidList, getValidListItems

app_name = "main"

urlpatterns = [
    path('', index),
    # POST
    path('user/add', createValidUser, name='createValidUser'),
    path('user/add/list', createValidList, name='createValidList'),
    path('user/add/list/item', createValidListItem, name='createValidListItem'),

    # GET
    path('user/<int:user_id>/get/list', getValidList, name='getValidList'),
    path('user/<int:user_id>/get/list/items/', getValidListItems, name='getValidListItems'),

    
]
