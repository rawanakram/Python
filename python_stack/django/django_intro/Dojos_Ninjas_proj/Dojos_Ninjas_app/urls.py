from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('dojo', views.addDojo),
    path('ninja', views.addNinja),
    path('delete', views.delete),
]