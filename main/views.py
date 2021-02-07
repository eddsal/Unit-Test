from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
            user =  UserAccount.objects.create(
                email=request.POST['email'],
                first_name=request.POST['firstName'],
                last_name=request.POST['lastName'],
                password=request.POST['password'],
                age=request.POST['age']
            )
            user.save()
            print('user have been succseful created')
    return HttpResponse('s')
        



    
