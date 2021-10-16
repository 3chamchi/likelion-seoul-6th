from django.contrib import admin

from .models import Photolog

@admin.register(Photolog)
class PhotologAdmin(admin.ModelAdmin):
    pass
