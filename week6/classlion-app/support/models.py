from django.db import models

# Create your models here.
class Support(models.Model):
    status_0 = ('결제 대기', '결제 대기')  # choices 사용을 위한 변수, [0]: 실제 DB 저장 값, [1]: 사용자에게 출력 값
    status_1 = ('결제 완료', '결제 완료')  # choices 사용을 위한 변수, [0]: 실제 DB 저장 값, [1]: 사용자에게 출력 값
    status_2 = ('취소', '취소')  # choices 사용을 위한 변수, [0]: 실제 DB 저장 값, [1]: 사용자에게 출력 값
    status_choices = (status_0,status_1,status_2)  # choice 생성
    # 클래스 class
    # 사용자 user
    # 상태(결제 완료, 취소, …) status
    status = models.CharField(  # 글자 수 제한적인 str() 필드
        max_length=5,  # CharField의 최대 크기 지정 -> DB에도 반영됨
        choices=status_choices  # 옵션 형태를 제공
    )
    # 지원자 이름 user_nickname
    user_nickname = models.CharField(  # 글자 수 제한적인 str() 필드
        max_length=30  # CharField의 최대 크기 지정 -> DB에도 반영됨
    )
    # 지원동기 motive
    motive = models.TextField()  # 글자 수 제한이 없는 긴 글
    # 만들고 싶은 서비스 want_service
    want_service = models.TextField()  # 글자 수 제한이 없는 긴 글
    # 선정 여부 is_pass
    is_pass = models.BooleanField(  # 참 또는 거짓의 필드, bool()
        default=False  # 필드의 기본 값 지정, 필드 자료형 값 입력
    )