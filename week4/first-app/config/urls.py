from django.contrib import admin  # 프로젝트 생성시 자동 생성 코드로 추후 설명
from django.urls import path  # 특정 URL 요청 시 처리를 위한 함수 연결 객체 => 'path는 url과 요청 처리 함수 연결'로 이해

<<<<<<< HEAD:week4/first-app/config/urls.py
from lotto.views import index as lotto_index
from calculator.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto_index),
    path('calculator/', index),
    # path('', index),
=======
from lotto.views import index as lotto_index  # lotto/ 요청 시 로또 번호 추출 처리해줄 lotto앱의 index 함수 임포트
from calculator.views import index as calculator_index  # calculator/ 요청 시 계산기 처리해줄 calculator앱의 index 함수 임포트


urlpatterns = [
    path('admin/', admin.site.urls),  # 프로젝트 생성시 자동 생성 코드로 추후 설명
    path('lotto/', lotto_index),  # http://127.0.0.1:8000/lotto/ 요청 시 처리 함수(lotto.views index) 연결
    path('calculator/', calculator_index),  # http://127.0.0.1:8000/calculator/ 요청 시 처리 함수(calculator.views index) 연결
    path('', calculator_index),  # 위와 동일한 처리 함수이나 요청 경로가 다름 http://127.0.0.1:8000/
>>>>>>> ad4b0e5d6e05c1815469330ea0e167b6d10d85fb:week4/config/urls.py
]
