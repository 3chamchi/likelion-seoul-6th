from datetime import datetime  # 현재 시간을 가져오기 위한 파이썬 모듈

from django.shortcuts import render, redirect, get_object_or_404  # 응답을 위한 장고 함수

from .models import Post  # 직접 작성한 Post 모델 불러오기


def list(request):  # Post 목록 요청을 처리하기 위한 응답 처리 함수
    post_all = Post.objects.all()  # Post 모델의 모든 데이터를 조회 post_all 변수에 할당
    context = {'post_all': post_all}  # 응답을 위한 context 변수 생성
    return render(request, 'list.html', context)  # list view에 응답


def detail(request, id):  # Post 목록의 글 상세 요청을 처리하기 위한 응답 처리 함수
    post = Post.objects.get(id=id)  # Post 모델의 특정 값을 조회하여 post 변수에 할당
    context = {'post': post}  # 응답을 위한 context 변수 생성
    return render(request, 'detail.html', context)  # 요청에 대한 응답


def new(request):  # 글 양식(Form) 요청을 처리하기 위한 응답 처리 함수
    return render(request, 'form.html')  # 요청에 대한 응답


def create(request):  # 글 생성 요청을 처리하기 위한 응답 처리 함수
    now = datetime.now()  # 작성 요청 시점을 저장하기 위한 현재 시간 now 변수에 할당
    # 클라이언트에서 Form에 입력한 name=title 값 title 변수에 저장
    title = request.POST['title']
    # 클라이언트에서 Form name이 content 값 content 변수에 저장
    content = request.POST['content']
    # 클라이언트에서 Form name이 created_by 값 created_by 변수에 저장
    created_by = request.POST['created_by']
    post = Post.objects.create(  # Post 모델의 데이터 생성
        title=title,  # Post 모델의 title 필드에 title 변수 값 전달
        content=content,  # Post 모델의 content 필드에 content 변수 값 전달
        created_by=created_by,  # Post 모델의 created_by 필드에 created_by 변수 값 전달
        created_at=now,  # Post 모델의 created_at 필드에 now 변수 값(현재시간) 전달
    )
    return redirect('/')
