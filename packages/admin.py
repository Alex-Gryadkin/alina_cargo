from django.contrib import admin
from .models import Packages, UserPackages
from import_export import resources
from datetime import datetime
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#admin.site.register(Packages)
admin.site.register(UserPackages)


class PackageResource(resources.ModelResource):

    class Meta:
        model = Packages
        skip_unchanged = True
        import_id_fields = ('id', )
        fields = ('id', 'status',)

class PackageAdmin(ImportExportModelAdmin):
    resource_classes = [PackageResource]

admin.site.register(Packages, PackageAdmin)