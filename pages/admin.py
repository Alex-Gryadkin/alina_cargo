from django.contrib import admin
from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','category','position')

admin.site.register(Page, PageAdmin)
admin.site.register(Category)