from django.contrib import admin  # 장고에서 제공하는 Admin 기능 사용을 위한 임포트

from .models import Post  # 직접 작성한 Post 모델 사용을 위한 임포트

@admin.register(Post)  # 어드민 사용을 위한 모델 연결
class PostAdmin(admin.ModelAdmin):  # 모델기반의 어드민 사용을 위한 상속
    list_display = ['id', 'title', 'content', 'created_at']  # 리스트 화면의 출력 필드 정의
    list_editable = ['title', ]  # 리스트 화면의 수정 필드 정의
    # list_filter = ['is_active', ]  # 리스트 화면의 필터 필드 정의
    search_fields = ['title',]  # 리스트 화면의 검색 필드 정의
    
    # python manage.py createsuperuser
