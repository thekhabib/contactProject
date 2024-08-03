from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'created_time', 'active')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email', 'body')
    list_filter = ('phone_number', 'email', 'created_time', )
    date_hierarchy = 'created_time'
    actions = ['disable_message', 'enable_message']

    def disable_message(self, request, queryset):
        queryset.update(active=False)

    def enable_message(self, request, queryset):
        queryset.update(active=True)
