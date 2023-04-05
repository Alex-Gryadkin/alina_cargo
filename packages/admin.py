from django.contrib import admin
from .models import Packages, UserPackages
# Register your models here.

admin.site.register(Packages)
admin.site.register(UserPackages)
