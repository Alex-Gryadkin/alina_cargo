from django.contrib import admin
from .models import Packages, UserPackages, Status, User
from .resources import PackageResource, PackageUserResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class PackageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'status', 'status_change_date_manual')
    search_fields = ['id']
    resource_classes = [PackageResource]


class StatusAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'order')


class PackageUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'desc', 'package_id', 'user_id')
    search_fields = ['desc', 'user_id__username', 'package_id__id']
    resource_classes = [PackageUserResource]


admin.site.register(Packages, PackageAdmin)
admin.site.register(UserPackages, PackageUserAdmin)
admin.site.register(Status, StatusAdmin)

