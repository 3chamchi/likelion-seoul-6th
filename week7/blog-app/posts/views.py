from datetime import datetime

from django.contrib.admin.decorators import register
from django.shortcuts import render

from .models import Post

def list(request):
    post_all = Post.objects.all()  # Post 모델의 전체 데이터 조회 
    context = {'post_all': post_all}  # 응답의 context 데이터 생성
    return render(request, 'list.html', context)  # 요청에 응답 함수, 'list.html'은 파일명이며 templates 폴더에 존재해야 함

def detail(request, id):
    post = Post.objects.get(id=id)  # Post 모델의 특정 데이터 조회
    context = {'post': post}
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'form.html')

def create(request):
    now = datetime.now()  # 현재 시간을 구하기 위한 함수
    title = request.POST['title']  # 클라이언트에서 POST 요청으로 넘어온 form의 name=title인 값을 title 변수에 할당
    content = request.POST['content']  # 클라이언트에서 POST 요청으로 넘어온 form의 name=content인 값을 content 변수에 할당
    created_by = request.POST['created_by']  # 클라이언트에서 POST 요청으로 넘어온 form의 name=created_by인 값을 created_by 변수에 할당
    post = Post.objects.create(
        title=title,  # Post 모델 title 필드에 title 변수 값 입력
        content=content,  # Post 모델 content 필드에 content 변수 값 입력
        created_by=created_by,  # Post 모델 created_by 필드에 created_by 변수 값 입력
        created_at=now,  # Post 모델 created_at 필드에 now 변수 값 입력
    )
    return render(request, 'list.html')