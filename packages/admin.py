from django.contrib import admin
from .models import Packages, UserPackages, Status
from .resources import PackageResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class PackageAdmin(ImportExportModelAdmin):
    list_display = ('id','status','status_change_date')
    resource_classes = [PackageResource]


class StatusAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'order')


admin.site.register(Packages, PackageAdmin)
admin.site.register(UserPackages)
admin.site.register(Status, StatusAdmin)
