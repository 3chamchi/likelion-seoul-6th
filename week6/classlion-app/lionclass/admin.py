from django.contrib import admin

from .models import LionClass

# python manage.py createsuperuser
@admin.register(LionClass)
class LionClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'price']
    list_filter = ['status']
    search_fields = ['title']