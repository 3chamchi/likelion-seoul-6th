from django.db import models

# Create your models here.
class LionClass(models.Model):
    status_1 = ('모집', '모집')  # choices 사용을 위한 변수, [0]: 실제 DB 저장 값, [1]: 사용자에게 출력 값
    status_2 = ('마감', '마감')  # choices 사용을 위한 변수, [0]: 실제 DB 저장 값, [1]: 사용자에게 출력 값
    status_choices = (status_1, status_2)  # choice 생성

    # 썸네일 이미지 파일 thumbnail image
    thumbnail_image = models.CharField(  # 글자 수 제한적인 str() 필드
        verbose_name='썸네일',  # 출력될 필드 이름
        max_length=300,  # CharField의 최대 크기 지정 -> DB에도 반영됨
        blank=True  # 빈값 가능 문자열 '' -> 빈값: '', null: None
    )
    # 상태(모집, 마감, …) status
    status = models.CharField(  # 글자 수 제한적인 str() 필드
        verbose_name='상태',  # 출력될 필드 이름
        max_length=2,  # CharField의 최대 크기 지정 -> DB에도 반영됨
        choices=status_choices,  # 옵션 형태를 제공
        help_text='교육과정의 상태입니다.'  # 도움말 텍스트
    )
    # 제목 title
    title = models.CharField(  # 글자 수 제한적인 str() 필드
        max_length=200  # CharField의 최대 크기 지정 -> DB에도 반영됨
    )
    # 요약 설명 title_description
    title_description = models.CharField(  # 글자 수 제한적인 str() 필드
        max_length=100  # CharField의 최대 크기 지정 -> DB에도 반영됨
    )
    # 금액 price
    price = models.IntegerField()  # 숫자 int() 필드
    # 클래스 소개 description
    description = models.TextField()  # 글자 수 제한이 없는 긴 글

    # python manage.py makemigrations
    # python manage.py migrate

    # 커리큘럼 curriculum
    # - 주차 week
    # - 강의 주제 lecture
    # FAQ faq
    # - 질문 questions
    # - 답변 answer