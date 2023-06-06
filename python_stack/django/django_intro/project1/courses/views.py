from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, name):
    return HttpResponse("Hello programmer"+ " " + name)