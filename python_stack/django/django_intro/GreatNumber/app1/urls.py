from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('guess', views.guess_method),
    path('reset', views.reset)

]
