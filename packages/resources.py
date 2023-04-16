from import_export import resources
from .models import Packages

class PackageResource(resources.ModelResource):
    class Meta:
        model = Packages
        skip_unchanged = True
        import_id_fields = ('id', )
        fields = ('id', 'status',)