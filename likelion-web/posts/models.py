from django.db import models


class Post(models.Model):

    title = models.CharField(
        verbose_name='제목',
        max_length=80,
    )

    content = models.TextField(
        verbose_name='내용',
    )

    created_at = models.DateTimeField(
        verbose_name='생성일',
        blank=True,
        null=True,
        help_text='데이터가 생성된 일자입니다.',
    )