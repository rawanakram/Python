from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def root(request):
    context = {
    	"all_the_users": Users.objects.all(),
    }
    return render(request, 'index.html', context)


def process(request):
    Users.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email_address=request.POST['email'], 
        age=request.POST['age'] )
    return redirect('/')