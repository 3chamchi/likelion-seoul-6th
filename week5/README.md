Model, Admin
---
[명령어](#명령어)  

[모델](#모델)  
* [모델 주요 필드](#모델-주요-필드)  

[어드민](#어드민)  
* [ModelAdmin 주요 옵션](#ModelAdmin-주요-옵션)  


## 명령어
* 모델 변경 사항 반영  
``` python manage.py makemigrations ```  

* 모델 DB 적용  
``` python manage.py migrate ```  

* 관리자 계정 생성  
``` python manage.py createsuperuser ```

## 모델 
* import 위치  
``` from django.db import models ```  

* 모델 생성을 위한 클래스(상속)  
``` models.Model ```  

### 모델 주요 필드
> 공식 문서 : (바로가기)[https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types]  

|필드명|자료형|설명|
|----|--|------|
|CharField|```str()```|작거나 큰 문자열을 위한 문자열 필드|
|TextField|```str()```|긴 텍스트 필드|
|IntegerField|```int()```|정수 필드(-2147483648to 값은 2147483647)|
|FloatField|```flot()```|부동 소수점 숫자 필드|
|BooleanField|```bool()```|참/거짓 필드|
|DateTimeField|```datatime()```|datetime.datetime인스턴스로 표시되는 날짜 및 시간 필드|

### 모델 필드 주요 옵션
> 공식 문서 : (바로가기)[https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options]  
  
|옵션|필드|값|설명|
|----|----|----|------|
|null|```모든 필드```|```True```, ```False```|None을 허용 여부|
|blank|```모든 필드```|```True```, ```False```|공백을 허용 여부|
|choices|```모든 필드```|```list(tuple())```|선택적인 값 입력|
|default|```모든 필드```|필드의 자료형 값|기본 값을 지정|
|help_text|```모든 필드```|```True```, ```False```|양식 위젯과 함께 표시할 추가 "도움말" 텍스트|
|unique|```모든 필드```|```True```, ```False```|해당 모델 간의 고유한 값의 여부|
|verbose_name|```모든 필드```|```str()```|사용자에게 노출될 문구|
|max_length|```CharField()```|```int()```|최대 글자 수의 제한|
|auto_now|```DateTimeField()```|```True```, ```False```|개체가 저장될 때마다 자동으로 필드를 지금으로 설정|
|auto_now_add|```DateTimeField()```|```True```, ```False```|개체가 처음 생성될 때 자동으로 필드를 지금으로 설정|  

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=80)
    # 내용
    content = models.TextField()
    # 생성일
    created_at =  models.DateTimeField()
    #python manage.py makemigrations
    #python manage.py migrate
```

## 어드민  
* 장고의핵심요소중하나모델중심의데이터관리  
* 프로젝트 콘텐츠를 관리할 수 있게 인터페이스를 제공  

* import
```from django.contrib import admin```  
  

### ModelAdmin 주요 옵션  

|옵션명|자료형|값|설명|
|----|----|----|------|
|list_editable|```list(str())```|모델 필드 이름|목록 페이지에서 편집을 허용할 모델의 필드 이름 목록으로 설정|
|list_display|```list(str())```|모델 필드 이름|목록 페이지에 표시되는 필드를 제어하도록 설정|
|list_filter|```list(str())```|모델 필드 이름|목록 페이지 오른쪽 사이드바에서 필터를 활성화하도록 설정|
|search_fields|```list(str())```|모델 필드 이름|목록 페이지에서 검색 상자를 활성화하도록 설정|

```python
from django.contrib import admin  # 장고에서 제공하는 Admin 기능 사용을 위한 임포트

from .models import Post  # 직접 작성한 Post 모델 사용을 위한 임포트

@admin.register(Post)  # 어드민 사용을 위한 모델 연결
class PostAdmin(admin.ModelAdmin):  # 모델기반의 어드민 사용을 위한 상속
    list_display = ['id', 'title', 'content', 'created_at']  # 리스트 화면의 출력 필드 정의
    list_editable = ['title', ]  # 리스트 화면의 수정 필드 정의
    # list_filter = ['is_active', ]  # 리스트 화면의 필터 필드 정의
    search_fields = ['title',]  # 리스트 화면의 검색 필드 정의
```