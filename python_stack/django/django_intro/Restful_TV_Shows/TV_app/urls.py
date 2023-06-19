from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.showAll),
    path('shows/new', views.newshow),
    path('creat', views.creatshow),
    path('shows/<show_id>', views.showdetails),
    path('shows/<int:show_id>/edit', views.editshow),
    path('update/<int:show_id>', views.updateshow),
    path('delete/<int:show_id>', views.deleteshow)
]

