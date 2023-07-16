from import_export import resources
from .models import Packages, UserPackages

class PackageResource(resources.ModelResource):
    class Meta:
        model = Packages
        skip_unchanged = True
        import_id_fields = ('id', )
        fields = ('id', 'status', 'status_change_date_manual')


class PackageUserResource(resources.ModelResource):
    class Meta:
        model = UserPackages
        skip_unchanged = True
        import_id_fields = ('id', )
        fields = ('id', 'desc', 'package_id', 'user_id')