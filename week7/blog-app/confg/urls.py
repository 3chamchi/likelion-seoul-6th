"""confg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import (list, detail, new, create)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list, name='list'),  # http://127.0.0.1:8000/ 으로 요청이 들어온 경우 list 함수로 처리, 응답
    path('<int:id>/', detail, name='detail'),  # url에 int형의 값이 들어올 수 있으며 그 값을 id로 선언
    path('new/', new, name='new'),  # new/ 요청 시 new 함수로 응답
    path('create/', create, name='create'),  # create/ 요청 시 new 함수로 응답
]
