from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        request.session['user_name'] = f'{fname} {lname}'
        request.session['status'] = f'registered'
        User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
        return redirect('/success')


def login(request):
    errors2 = User.objects.login_validator(request.POST)
    print(errors2)
    if len(errors2) > 0:
        for key, value in errors2.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.filter(email=request.POST['email2'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
                request.session['user_name'] = logged_user.first_name
                request.session['status'] = f'logged in'
        return redirect('/success')


def success(request):
    context={
        'user_name': request.session['user_name'],
        'status':request.session['status'],
    }
    return render(request, 'success.html', context)


def logout(request):
    del request.session['user_name']
    del request.session['status']
    request.session.flush()
    return redirect('/')