from django.contrib import admin
from six import add_metaclass
# from django.contrib.auth.models import User
from .models import Profile

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email_confirmed', 'is_admin']