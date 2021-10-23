from django.contrib import admin

from .models import DogImage


@admin.register(DogImage)
class DogImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')

# from django.db.models import Q
# search_str = ''
# Compay_Data.objects.filter(
#     Q(name=search_str) |
#     Q(지역=search_str) |
#     Q(product_set__카테고리__dwd=search_str)
# )
# 키워드 : lookup, Q 객체