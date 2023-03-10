from django.contrib import admin
from . models import *

@admin.register(Pet_info)
class Pet_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet_owner', 'pet_name'] 


@admin.register(Pet_diet_set)  
class Pet_diet_set_Admin(admin.ModelAdmin): 
    list_display = ['id', 'pet_name']
admin.site.register(Pet_daily_feed)  