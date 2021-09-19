from django.db import models

# Create your models here.
class LionClass(models.Model):
    status_1 = ('모집', '모집')
    status_2 = ('마감', '마감')
    status_choices = (status_1, status_2)

    # 썸네일 이미지 파일 thumbnail image
    thumbnail_image = models.CharField(verbose_name='썸네일', max_length=255, blank=True)
    # 상태(모집, 마감, …) status
    status = models.CharField(verbose_name='상태', max_length=2, choices=status_choices)
    # 제목 title
    title = models.CharField(verbose_name='제목', max_length=300, help_text='300자 이하의 텍스트를 입력해주세요.')
    # 요약 설명 title_description
    title_description = models.CharField(max_length=100)
    # 금액 price
    price = models.IntegerField(help_text='1원 이상의 숫자를 입력해주세요.')
    # 클래스 소개 description
    description = models.TextField()

    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py createsuperuser

    # 커리큘럼 curriculum
    # - 주차 week
    #   - 강의 주제 lecture
    # FAQ faq
    # - 질문 questions
    # - 답변 answer