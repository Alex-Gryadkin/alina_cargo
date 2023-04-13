from django.contrib import admin
from .models import Packages, UserPackages
from .resources import PackageResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(UserPackages)
class PackageAdmin(ImportExportModelAdmin):
    list_display = ('id','status','status_change_date')
    resource_classes = [PackageResource]

admin.site.register(Packages, PackageAdmin)