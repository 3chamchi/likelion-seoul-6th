<<<<<<< HEAD
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
=======
from datetime import datetime

from django.contrib.admin.decorators import register
from django.shortcuts import render, redirect

from .models import Post

def delete(request, id):
    context = {}
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    else:
        context.update(post=post)
        return render(request, 'confirm_delete.html', context)

def update(request, id):
    context = {'title':'글 수정', 'submit_text': '수정하기'}
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        created_by = request.POST['created_by']
        
        post.title = title
        post.content = content
        post.created_by = created_by
        post.save()
        return redirect('detail', id)
    else:
        context.update(post=post)
        return render(request, 'form.html', context)
        
        

def list(request):
    post_all = Post.objects.all()  # Post 모델의 전체 데이터 조회 
    context = {'post_all': post_all}  # 응답의 context 데이터 생성
    return render(request, 'list.html', context)  # 요청에 응답 함수, 'list.html'은 파일명이며 templates 폴더에 존재해야 함

def detail(request, id):
    post = Post.objects.get(id=id)  # Post 모델의 특정 데이터 조회
    context = {'post': post}
    return render(request, 'detail.html', context)

def new(request):
    context = {'title':'글 등록', 'submit_text': '등록하기'}
    return render(request, 'form.html', context)

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
    return redirect('/')
>>>>>>> main
