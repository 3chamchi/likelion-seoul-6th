from django.db import models  # 장고 모델을 사용하기 위한 임포트


class Post(models.Model):  # 장고 모델 Post 작성
    title = models.CharField(verbose_name='제목', max_length=80)  # Post 모델의 게시글 제목 속성 정의
    content = models.TextField(verbose_name='내용',)  # Post 모델의 게시글 내용 속성 정의
    created_at = models.DateTimeField(
        verbose_name='생성일', blank=True, null=True, help_text='데이터가 생성된 일자입니다.',)  # Post 모델의 생성일 속성 정의
    created_by = models.CharField(verbose_name='작성자', max_length=30, blank=True, help_text='게시글 작성자입니다.')  # Post 모델의 작성자 속성 정의
    is_view = models.BooleanField(verbose_name='공개 여부', default=True, help_text='비공개 시 체크를 해제해주세요.')  # Post 모델의 공개 여부 속성 정의
