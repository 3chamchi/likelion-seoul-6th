from django.db import models

# Create your models here.
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=80)

    # 내용
    content = models.TextField()

    # 생성일
    created_at = models.DateTimeField(blank=True, null=True)
    # python manage.py makemigrations
    # python manage.py migrate