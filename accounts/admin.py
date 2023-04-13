from django.contrib import admin
from accounts.models import Cities, CargoUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Cities)
admin.site.register(CargoUser)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
