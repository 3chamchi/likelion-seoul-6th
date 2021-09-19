from django.contrib import admin

from .models import Support

# Register your models here.
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['status', 'user_nickname', 'is_pass']
    list_filter = ['status', 'is_pass']
    search_fields = ['user_nickname']