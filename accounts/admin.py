from django.contrib import admin, messages
from accounts.models import Cities, CargoUser
from django.utils.translation import ngettext
from django.db.models import F
from django.contrib import admin
from .resources import UserResource
from import_export.admin import ImportExportModelAdmin
from .models import User


@admin.action(description="Активировать")
def make_active(self, request, queryset):
    updated = queryset.update(is_activated=True)
    self.message_user(
        request,
        ngettext(
            "%d код был успешно активирован.",
            "Кодов было успешно активировано: %d.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="Деактивировать")
def make_not_active(self, request, queryset):
    updated = queryset.update(is_activated=False)
    self.message_user(
        request,
        ngettext(
            "%d код был успешно деактивирован.",
            "Кодов было успешно деактивировано: %d.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class CagroAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_activated', 'cargo_code', 'last_login')
    search_fields = ['username__username', 'cargo_code']
    actions = [make_active, make_not_active]

    def get_queryset(self, request):
        qs = super(CagroAdmin, self).get_queryset(request)
        qs = qs.annotate(last_login=F('username__last_login'))
        return qs

    def last_login(self, obj):
        return obj.last_login

    last_login.admin_order_field = 'last_login'


class UsersAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'password', 'username')


admin.site.register(Cities)
admin.site.unregister(User)
admin.site.register(User, UsersAdmin)
admin.site.register(CargoUser, CagroAdmin)
