from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/feeddata', views.json_open, name = 'json'),
]