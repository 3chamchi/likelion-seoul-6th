from django.contrib import admin
from django.urls import path, include

from posts.views import list

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', list, name='home'),  # 메인 페이지 지정

    path('accounts/', include('accounts.urls')),  # accounts 앱의 urls 사용
    path('posts/', include('posts.urls')),  # posts 앱의 urls 사용
]
