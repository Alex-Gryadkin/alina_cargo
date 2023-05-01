from import_export import resources
from .models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        skip_unchanged = True
        import_id_fields = ('id', 'password', 'username')
        fields = ('id', 'password', 'username')

