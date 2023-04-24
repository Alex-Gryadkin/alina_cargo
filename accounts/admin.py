from django.contrib import admin, messages
from accounts.models import Cities, CargoUser
from django.utils.translation import ngettext
from django.db.models import F


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
    list_display = ('username', 'is_activated', 'cargo_code', 'last_login')
    actions = [make_active, make_not_active]

    def get_queryset(self, request):
        qs = super(CagroAdmin, self).get_queryset(request)
        qs = qs.annotate(last_login=F('username__last_login'))
        return qs

    def last_login(self, obj):
        return obj.last_login

    last_login.admin_order_field = 'last_login'


admin.site.register(Cities)
admin.site.register(CargoUser, CagroAdmin)
