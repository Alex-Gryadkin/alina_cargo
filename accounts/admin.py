from django.contrib import admin, messages
from accounts.models import Cities, CargoUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ngettext


@admin.action(description="Активировать")
def make_active(self, request, queryset):
    updated = queryset.update(is_activated=True)
    self.message_user(
        request,
        ngettext(
            "%d пользователь был успешно активирован.",
            "%d пользователей было успешно активмировано.",
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
            "%d пользователь был успешно деактивирован.",
            "%d пользователей было успешно деактивмировано.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class CagroAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_activated', 'cargo_code', 'get_last_login')
    actions = [make_active, make_not_active]


admin.site.register(Cities)
admin.site.register(CargoUser, CagroAdmin)
