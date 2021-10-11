from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    """ 게시글 모델 """
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

class Comment(models.Model):
    """ 댓글 모델 """
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)


class Scrap(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)