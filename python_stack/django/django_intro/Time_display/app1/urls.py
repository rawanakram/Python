from django.urls import path
from . import views


urlpatterns = [
    path('', views.Time_and_Date)
    
]