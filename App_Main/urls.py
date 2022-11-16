from django.urls import path
from .views import *
app_name='App_Main'

urlpatterns = [
    path('', Main_Home, name = 'home'),
    path('pet/info',Pet_info_View, name = 'pet'),  
    path('pet/info/create', Pet_create_View, name = 'pet_create'),
    path('pet/info/update', Pet_update_View, name  = 'pet_update'),
    path('pet/statistics', Pet_statistics_View, name = 'pet_statistics'),
    path('pet/diet/info', Pet_info_View, name = 'pet_diet_info'),
    path('pet/diet/set', Pet_diet_set_View, name = 'pet_diet_set'),
    path('pet/diet/update', Pet_diet_set_View, name = 'pet_diet_update')
]

