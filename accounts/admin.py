from django.contrib import admin, messages
from accounts.models import Cities, CargoUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ngettext

admin.site.register(Cities)
admin.site.register(CargoUser)

@admin.action(description="Make active")
def make_active(self, request, queryset):
    updated = queryset.update(is_active=True)
    self.message_user(
        request,
        ngettext(
            "%d user was successfully set active.",
            "%d users were successfully set active.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )
@admin.action(description="Make not active")
def make_not_active(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(
        request,
        ngettext(
            "%d user was successfully set NOT active.",
            "%d users were successfully set NOT active.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_active', 'is_staff', 'last_login') # Added last_login
    actions = [make_active,make_not_active]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
