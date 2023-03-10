from django.contrib import admin
from . models import User
# Register your models here.

@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display = ['id', 'email', 'user_name']