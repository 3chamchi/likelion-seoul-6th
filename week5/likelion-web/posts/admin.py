from django.contrib import admin  # 장고 어드민을 사용하기 위한 임포트

from .models import Post  # Post 모델 사용을 위한 임포트, 점(.)은 현재 파일의 위치를 나타냄


@admin.register(Post)  # 장고 어드민에 Post 모델 등록, @함수명() -> 데코레이터 함수
class PostAdmin(admin.ModelAdmin):  # 장고 어드민 ModelAdmin 클래스 상속
    list_display = ('title', 'content', 'created_at',)  # 목록 페이지에서 보여줄 속성 지정