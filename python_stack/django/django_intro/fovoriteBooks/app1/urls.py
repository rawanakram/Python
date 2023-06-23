from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('books/<int:id>', views.book_details),
    path('books/<int:id>/update', views.update),
    path('books/<int:id>/delete', views.delete),
    path('books/<int:id>/addFavorite', views.addFavorite),
    path('books/<int:id>/unfavorite', views.unfavorite)
]