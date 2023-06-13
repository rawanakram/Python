from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def root(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()
    
    context = {
        "dojos":dojos,
        "ninjas":ninjas,   
    }
    return render (request, 'index.html', context)


def addDojo(request):
    Dojo.objects.create(
    name = request.POST['name'],
    city = request.POST['city'],
    state = request.POST['state'],
    )
    return redirect('/')


def addNinja(request):
    Ninja.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    dojo_id = request.POST['dojo'],
    )
    return redirect('/')


def delete(request):
    dojo = Dojo.objects.get(id=request.POST['del'])
    dojo.delete()
    return redirect('/')