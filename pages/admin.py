from django.contrib import admin
from .models import Page, Category
from django_summernote.admin import SummernoteModelAdmin


class PageAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','category','position')
    summernote_fields = ('content',)


admin.site.register(Page, PageAdmin)
admin.site.register(Category)
