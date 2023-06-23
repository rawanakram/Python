from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'loginreg.html')


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
        user = User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
        request.session['user_id'] = user.id
        print(request.session['user_id'])
        return redirect('/books')


def login(request):
    errors2 = User.objects.login_validator(request.POST)
   
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
                request.session['user_id'] = logged_user.id
                request.session['status'] = f'logged in'
        print(request.session['user_id'])
        return redirect('/books')


def books(request):
    this_user = User.objects.filter(id=request.session['user_id'])
    context={
        'user_name': request.session['user_name'],
        'status':request.session['status'],
        'all_books':Book.objects.all(),
        'all_users':User.objects.all(),
        'user':this_user[0]
    }
    return render(request, 'books.html', context)


def logout(request):
    del request.session['user_name']
    del request.session['status']
    request.session.flush()
    return redirect('/')



def add_book(request):
    errors3 = Book.objects.book_validator(request.POST)
    
    if len(errors3) > 0:
        for key, value in errors3.items():
            messages.error(request, value)
        return redirect('/books')

    else:
        user_upload = User.objects.get(id= request.session['user_id'])
        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            uploaded_by = user_upload)
        user_upload.liked_books.add(book)
        return redirect('/books')


def book_details(request, id):
    current_user = User.objects.get(id= request.session['user_id'])
    book = Book.objects.get(id = id)
    context={
        'current_user': current_user,
        'book':book,
        'all_users':User.objects.all(),
        'all_books':Book.objects.all()
    }
    return render(request, 'book_details.html', context)


def update(request, id):
    errors3 = Book.objects.book_validator(request.POST)
    
    if len(errors3) > 0:
        for key, value in errors3.items():
            messages.error(request, value)
        return redirect(f'/books/{id}')

    else:
        book_update = Book.objects.get(id=id)
        book_update.title = request.POST['title']
        book_update.description = request.POST['description']
        book_update.save()
        return redirect('/books')


def delete(request, id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()
    return redirect('/books')


def addFavorite(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id= request.session['user_id'])
    user.liked_books.add(book)
    return redirect('/books')


def unfavorite(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id= request.session['user_id'])
    user.liked_books.remove(book)
    return redirect('/books')