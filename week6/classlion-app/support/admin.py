from django.contrib import admin

from .models import Support

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['user_nickname', 'status', 'is_pass']
    list_filter = ['status', 'is_pass']
    search_fields = ['user_nickname']