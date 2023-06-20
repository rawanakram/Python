from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    all_courses = Course.objects.all()

    context = {
        'all_courses':all_courses,
    }
    return render(request, 'index.html', context)


def add(request):
    errors = Course.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    
        return redirect('/')

    else:
        course = Course.objects.create(
            name = request.POST['name'],
            description = request.POST['description']
        )
        return redirect('/')


def destroy(request, id):
    all_courses = Course.objects.all()
    course = Course.objects.get(id=id)
    context = {
        'all_courses':all_courses,
        'course':course
    }
    return render(request, 'delete.html', context)


def delete(request, id):
    course = Course.objects.get(id=int(id))
    course.delete()
    return redirect('/')