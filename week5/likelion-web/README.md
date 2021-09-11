Django(3) - 템플릿, 모델, 어드민
---
## 목차
[1. 템플릿(Template)](#1-템플릿(Template))  
[2. 모델(Model)](#2-모델(Model))  
[3. 어드민(Admin)](#3-어드민(Admin))  

## 1. 템플릿(Template)
* 데이터 출력을 위해 사용
* html에서 파이썬 유사 문법을 사용할 수 있게 하는 역할

### 1-1. 템플릿 언어
|구분|템플릿 언어|내용|비고|
|:----:|:-------:|:--------|:----:|
|변수|```{{ 변수명 }}```| View에서 Context로 전달 변수 사용||
|태그|```{% if 조건문 %} … {% endif %}```|View Context로 전달된||
|태그|```{% for value in value_list %} … {% endfor %}```|View에서 Context로 전달 변수로 반복문 사용||
|주석|```{# … #}```|코드 주석 ```<!-- -->``` HTML 주석은 노출되지만 템플릿 언어 주석은 노출되지 않음||
|필터|```{{ value\|truncatechars:7 }} ```|지정된 문자 수보다 긴 경우 문자열을 자릅니다. 잘린 문자열은 번역 가능한 줄임표 문자("...") 출력||
|필터|```{{ value\|lower }}```|문자열 value를 모두 소문자로 변환||
|필터|```{{ value\|slice:":2" }}```|리스트 형태의 자료형을 슬라이싱||
|필터|```{{ value\|date:"D d M Y" }}```|시간 데이터를 날짜 형식 지정||

## 2. 모델(Model)
* 데이터를 관리하는 역할
### 2-1. 주요 필드
|필드명|자료형|설명|비고|
|:----:|:-------:|:--------|:----:|
|```CharField```|```str()```|작거나 큰 문자열을 위한 문자열 필드||
|```TextField```|```str()```|긴 텍스트 필드, 여러번 줄변경을 하거나 게시판의 본문 내용 같은 데이터||
|```BooleanField```|```bool()```|참/거짓 필드||
|```DateTimeField```|```datetime()```|datetime.datetime인스턴스로 표시되는 날짜 및 시간 필드||
|```IntegerField```|```int()```|정수 필드(-2147483648to 값은 2147483647)||
|```FloatField```|```float()```|부동 소수점 숫자 필드||
> 공식문서 : https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types

### 2-2. 필주 주요 속성
|속성명|필드|값|설명|
|:----:|:-------:|:--------:|:----|
|```null```|모든 필드|```True```, ```False```|None을 허용 여부|
|```blank```|모든 필드|```True```, ```False```|공백을 허용 여부|
|```choices```|모든 필드|```list(tuple())```|선택적인 값 입력|
|```default```|모든 필드|필드의 자료형 값|기본적인 값을 지정|
|```unique```|모든 필드|```True```, ```False```|해당 모델 간의 고유한 값의 여부|
|```verbose_name```|모든 필드|```str()```|사용자에게 노출될 문구|
|```max_length```|```CharField```|```int()```|최대 글자 수의 제한|
> ※ 공식문서 : https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields

## 3. 어드민(Admin)
* 장고의 핵심 요소 중 하나 모델 중심의 데이터 관리
* 프로젝트 콘텐츠를 관리할 수 있게 인터페이스를 제공  

### 3-1. 주요 속성
|속성명|설명|비고|
|:----:|:----------:|:----:|
|```list_display```|목록 페이지에 표시되는 필드를 제어하도록 설정 합니다.|
|```list_editable```|목록 페이지에서 편집을 허용할 모델의 필드 이름 목록으로 설정 합니다.|
|```list_filter```|목록 페이지 오른쪽 사이드바에서 필터를 활성화하도록 설정 합니다|
|```search_fields```|목록 페이지에서 검색 상자를 활성화하도록 설정 합니다.|
> ※ 공식문서 : https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
