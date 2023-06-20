from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('courses/destroy/<int:id>', views.destroy),
    path('delete/<int:id>', views.delete)
]