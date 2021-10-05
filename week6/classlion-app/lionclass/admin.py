from django.contrib import admin  # 장고 Admin 사용을 위한 임포트

from .models import LionClass  # LionClass 사용을 위한 임포트

@admin.register(LionClass)  # Admin에 LionClass 연결
class LionClassAdmin(admin.ModelAdmin):  # Admin 기능(코드) 사용을 위한 임포트
    list_display = ['title', 'status', 'price']  # 목록 화면 출력을 위한 필드 설정
    list_filter = ['status']  # 목록 화면 필터 필드 설정
    search_fields = ['title']  # 목록 화면 검색 필드 설정