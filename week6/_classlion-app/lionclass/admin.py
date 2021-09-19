from django.contrib import admin

from .models import LionClass

# Register your models here.
@admin.register(LionClass)
class LionClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_description', 'price', 'status']
    list_filter = ['status']
    search_fields = ['title']