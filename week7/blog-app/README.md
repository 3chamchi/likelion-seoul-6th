CRUD App
---
C : Create  
R : Read  
U : Update  
D : Delete  

가상환경 생성 및 프로젝트 생성
## 1. 프로젝트 폴더 생성  
* 

## 2. 가상환경 생성  
```python -m venv venv```  

## 3. 가상환경 접속  
* 맥  
```source vevn/bin/activate```  
* 윈도우  
```venv\Scripts\activate```  
접속 후 터미널 ```(venv)``` 확인
## 4. 장고 설치  
* pip 업그레이드  
```pip install --upgrade pip```  
* 장고 설치  
```pip install django```  
설치 후 ```pip list``` 패키지 설치 확인  
```
Package           Version
----------------- --------
asgiref           3.4.1
Django            3.2.7
pip               21.2.4
pytz              2021.1
setuptools        47.1.0
sqlparse          0.4.2
typing-extensions 3.10.0.2
```

## 5. 장고 프로젝트 생성  
* 생성 전 확인 사항
   * 가상환경 접속 상태 확인 : ```(venv)```
   * 현재 디렉토리 경로 확인  
      * 맥 : ```pwd```, ```ls```
      * 윈도우 : ```cd ,```, ```dir```  
* 장고 프로젝트 생성 
```django-admin startproject config .```  
   * 장고 프로 젝트 생성 후
      * 맥 : ```ls```  
      * 윈도우 : ```dir```  
      * 파일 목록 : ```config    manage.py venv```

## 6. posts 앱 생성 및 모델, 어드민 작성
```django-admin startapp posts```
* 앱 생성 후 파일 확인
   * 맥 : ```ls```  
   * 윈도우 : ```dir```
   * 파일 목록 : ```config    manage.py posts     venv```
* 앱 등록, config/settings.py
```python
# 생략
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',  # posts 앱 등록
]
# 생략
```  

* models.py 작성, posts/models.py
    * 필드 : 제목, 내용, 작성자, 작성일, 공개 여부
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(
        verbose_name='제목',
        max_length=80,
    )

    content = models.TextField(
        verbose_name='내용'
    )

    created_at = models.DateTimeField(
        verbose_name='작성일'
    )

    created_by = models.CharField(
        verbose_name='작성자',
        max_length=100
    )

    is_view = models.BooleanField(
        verbose_name='공개 여부',
        default=True
    )
```  

* 모델 작성 후 마이그레이션 및 DB 반영  
```python manage.py makemigrations```  
```python manage.py migrate```  

* admin.py 작성, posts.admin.py
```python
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'title', 'is_view', 'created_at']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'created_by', 'title']

```

## 7. 데이터베이스 생성 및 관리자 계정 생성
* models.py 파일의 변경내용을 기록  
```
python manage.py makemigrations
```  
* posts/migrations의 파일을 기준으로 데이터베이스 반영
```
python manage.py migrate
```  
* 관리자 계정 생성  
```python manage.py createsuperuser```
   * 참고사항 : password 입력 시 입력 값이 보이지 않음