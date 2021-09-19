from django.db import models

# Create your models here.
class Support(models.Model):
    status_0 = ('결제 대기', '결제 대기')
    status_1 = ('결제 완료', '결제 완료')
    status_2 = ('취소', '취소')
    status_choices = (status_0, status_1, status_2)
    # 클래스 class
    # 사용자 user
    # 상태(결제 완료, 취소, …) status
    status = models.CharField(verbose_name='상태', max_length=5, choices=status_choices)
    # 지원자 이름 user_nickname
    user_nickname = models.CharField(verbose_name='지원자 이름', max_length=25)
    # 지원동기 motive
    motive = models.TextField(verbose_name='지원동기')
    # 만들고 싶은 서비스 want_service
    want_service = models.TextField(verbose_name='만들고 싶은 서비스')
    # 선정 여부 is_pass
    is_pass = models.BooleanField(verbose_name='선정 여부', default=True)

    # python manage.py makemigrations
    # python manage.py migrate