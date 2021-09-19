ClassLion Model, Admin
---
[명령어](#명령어)  

[코드 작성 파일](#코드-작성-파일)  
[config](#config)
* [settings.py](#settingspy)  

[LionClass App](#lionclass-app)  
* [models.py](#modelspy)  
* [admin.py](#adminpy)  

[Support App](#support-app)  
* [models.py](#modelspy)  
* [admin.py](#adminpy)  


# 명령어
migrations 파일 생성 : models.py 변경사항 적용  
```python manage.py makemigrations```

migrate 실행 : migration 파일로 DB 반영  
```python manage.py migrate```

관리자 계정 생성  
```python manage.py createsuperuser```
# 코드 작성 파일  

## config  
### settings.py  
```python
# 생략

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lionclass',  # 생성한 App 추가
    'support',  # 생성한 App 추가
]
# 생략
```
## LionClass App

### models.py
```python
from django.db import models

# Create your models here.
class LionClass(models.Model):
    status_1 = ('모집', '모집')
    status_2 = ('마감', '마감')
    status_choices = (status_1, status_2)

    # 썸네일 이미지 파일 thumbnail image
    thumbnail_image = models.CharField(verbose_name='썸네일', max_length=300, blank=True)
    # 상태(모집, 마감, …) status
    status = models.CharField(verbose_name='상태', max_length=2, choices=status_choices, help_text='교육과정의 상태입니다.')
    # 제목 title
    title = models.CharField(max_length=200)
    # 요약 설명 title_description
    title_description = models.CharField(max_length=100)
    # 금액 price
    price = models.IntegerField()
    # 클래스 소개 description
    description = models.TextField()

    # python manage.py makemigrations
    # python manage.py migrate

    # 커리큘럼 curriculum
    # - 주차 week
    # - 강의 주제 lecture
    # FAQ faq
    # - 질문 questions
    # - 답변 answer
```
### admin.py
```python
from django.contrib import admin

from .models import LionClass

# python manage.py createsuperuser
@admin.register(LionClass)
class LionClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'price']
    list_filter = ['status']
    search_fields = ['title']
```
## Support App
### models.py
```python
from django.db import models

# Create your models here.
class Support(models.Model):
    status_0 = ('결제 대기', '결제 대기')
    status_1 = ('결제 완료', '결제 완료')
    status_2 = ('취소', '취소')
    status_choices = (status_0,status_1,status_2)
    # 클래스 class
    # 사용자 user
    # 상태(결제 완료, 취소, …) status
    status = models.CharField(max_length=5, choices=status_choices)
    # 지원자 이름 user_nickname
    user_nickname = models.CharField(max_length=30)
    # 지원동기 motive
    motive = models.TextField()
    # 만들고 싶은 서비스 want_service
    want_service = models.TextField()
    # 선정 여부 is_pass
    is_pass = models.BooleanField(default=False)
```
### admin.py
```python
from django.contrib import admin

from .models import Support

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['user_nickname', 'status', 'is_pass']
    list_filter = ['status', 'is_pass']
    search_fields = ['user_nickname']
```