from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path('', views.index, name='index'),
    path('another/', Another.as_view()),
]
