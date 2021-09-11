from django.db import models  # 장고 모델을 사용하기 위한 임포트


class Post(models.Model):  # 장고 모델 Post 작성
    title = models.CharField(verbose_name='제목', max_length=80,)  # Post 모델의 title 속성 정의
    content = models.TextField(verbose_name='내용',)  # Post 모델의 content 속성 정의
    created_at = models.DateTimeField(
        verbose_name='생성일', blank=True, null=True, help_text='데이터가 생성된 일자입니다.',)  # Post 모델의 created_at 속성 정의
