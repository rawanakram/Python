from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookForm),
    path('addbook', views.addbook),
    path('books/<int:book_id>', views.viewbook),
    path('add_auther', views.add_auther_to_book),
    path('authers', views.autherForm),
    path('addauther', views.addauther),
    path('authers/<auther_id>', views.viewauther),
    path('add_book', views.add_book_to_auther),
]