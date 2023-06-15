from django.shortcuts import render, redirect
from .models import Book, Auther

# Create your views here.
def bookForm(request):
    all_books = Book.objects.all()
    all_authers = Auther.objects.all()

    context = {
        "all_books":all_books,
        "all_authers":all_authers
    }
    return render (request, 'index.html', context)


def addbook(request):
    Book.objects.create(
    title = request.POST['title'],
    desc = request.POST['description']
    )
    return redirect('/')


def viewbook(request, book_id):
    book =Book.objects.get(id=book_id)
    all_book_authers =book.authers.all()
    all_authers = Auther.objects.all()
    context = {
        "book":book,
        'all_book_authers':all_book_authers,
        'all_authers':all_authers
    }
    return render(request, 'view_book.html', context)


def add_auther_to_book(request):
    auther_id = request.POST['authers']
    book_id = request.POST['books']
    auther_to_add= Auther.objects.get(id = auther_id)
    book= Book.objects.get(id = book_id)
    book.authers.add(auther_to_add)
    
    return redirect('/books/' + book_id)


def autherForm(request):
    all_authers = Auther.objects.all()
    context = {
        "all_authers":all_authers
    }
    return render (request, 'auther.html', context)


def addauther(request):
    Auther.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    notes = request.POST['notes']
    )
    return redirect('/authers')


def viewauther(request, auther_id):
    auther = Auther.objects.get(id=auther_id)
    all_auther_books =auther.books.all()
    all_books = Book.objects.all()
    context = {
        "auther":auther,
        'all_auther_books':all_auther_books,
        'all_books':all_books
    }
    return render(request, 'view_auther.html', context)


def add_book_to_auther(request):

    auther_id = request.POST['authers']
    book_id = request.POST['books']
    book_to_add= Book.objects.get(id = book_id)
    auther= Auther.objects.get(id = auther_id)
    auther.books.add(book_to_add)

    return redirect('/authers/' + auther_id)
