import random  # 랜덤 값을 추출하기 위한 모듈 임포트

from django.shortcuts import render  # Template(html)을 응답하기 위한 함수 임포트


def index(request):
    """ 로또 번호 추첨 요청을 처리하기 위한 함수 """
    lotto_number = random.sample(range(1, 46), 7)  # 로또 번호 추출, random.sample(x, y) 함수는 리스트 x에서 랜덤한 y의 수를 추출
    context = {  # 응답 시 context 변수 
        'lotto_number': lotto_number,  # 딕셔너리 형태, key값은 Template에서 사용하기 위한 변수명
    }
    return render(request, 'lotto.html', context)  # 요청에 응답, 실질적 응답 전 Template Engine 실행
