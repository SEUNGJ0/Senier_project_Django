from django.urls import path
from .views import *
app_name='App_Main'

urlpatterns = [
    path('', Main_Home, name = 'home'),
    path('pet/',Pet_info_View, name = 'pet'),  
    path('pet/create', Pet_create_View, name = 'pet_create'),
    path('pet/update', Pet_update_View, name  = 'pet_update'),
    path('pet/statistics', Pet_statistics_View, name = 'pet_statistics')
]

