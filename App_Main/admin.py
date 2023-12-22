from django.contrib import admin
from . models import *

@admin.register(Pet_info)
class Pet_info_Admin(admin.ModelAdmin):
    list_display = ['id', 'pet_owner', 'pet_name'] 


@admin.register(Pet_diet_set)  
class Pet_diet_set_Admin(admin.ModelAdmin): 
    list_display = ['id', 'pet_name']

@admin.register(Pet_daily_feeding)  
class Pet_daily_feeding_Admin(admin.ModelAdmin):
    list_display = ['pet_name','feed_date','feed_time','feed_index']
    list_filter = ['pet_name', 'feed_date']
