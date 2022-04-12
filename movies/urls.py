from django.urls import path
from . import views

urlpatterns = [
    path('first', views.index, name='index'),
]
