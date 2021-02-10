from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from main.models import *
from main.utils import *


def index(request):
    context: {}
    return HttpResponse('index Page')

@csrf_exempt
def createValidUser(request):
    if request.method == "POST":
        dic = {
            'firstName': request.POST['firstName'],  
            'lastName' : request.POST['lastName'],
            'age' :request.POST['age'],
            'password' : request.POST['password'],
            'email' :request.POST['email']
        }
        if isValid(dic):
            user = UserAccount(
                email=request.POST['email'],
                age=request.POST['age'],
                first_name=request.POST['firstName'],
                last_name=request.POST['lastName'],
                password=request.POST['password'],
            )
            user.save()
        else:
            raise SuspiciousOperation
    return HttpResponse('user has been created successfully')
        


@csrf_exempt
def createValidList(request):
    if request.method == "POST":
        user = UserAccount.objects.get(email=request.POST['email'])
        user.listt = List.objects.create(name="TODILIST")
        user.save()
    return HttpResponse('list has been created successfully')
        