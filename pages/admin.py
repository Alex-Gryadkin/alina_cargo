from django.contrib import admin
from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category)