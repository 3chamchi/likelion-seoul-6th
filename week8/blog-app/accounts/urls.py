from django.urls import path
from .views import signup, login, logout  # 요청을 넘길 함수 불러오기

app_name = 'accounts'  # 템플릿 url 태그 사용 시 네임스페이스 지정

urlpatterns = [
		path('signup/', signup, name='signup'),  # accounts/signup/ url 요청 시 signup 함수로 전달
		path('login/', login, name='login'),  # accounts/login/ url 요청 시 login 함수로 전달
		path('logout/', logout, name='logout'),  # accounts/logout/ url 요청 시 logout 함수로 전달
]
