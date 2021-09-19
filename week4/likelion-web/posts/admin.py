from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_editable = ['title']
    list_filter = []
    search_fields = ['title']
    # python manage.py createsuperuser