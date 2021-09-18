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