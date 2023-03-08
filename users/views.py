from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return HttpResponse("<h1> Hello </h1>", request)

def home(request):
    return render(request,'users/home.html')