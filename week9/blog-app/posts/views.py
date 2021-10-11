from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, Comment, Scrap

@login_required  # 로그인한 경우에만 허용
def scrap(request, id):
    post = get_object_or_404(Post, id=id)
    scrap_filter = Scrap.objects.filter(user=request.user, post=post)
    if len(scrap_filter) < 1:
        Scrap.objects.create(user=request.user, post=post)
    else:
        scrap_filter.delete()

    url = request.META.get('HTTP_REFERER', '/')
    return redirect(url)
    

def comment_create(request, id):
    post = get_object_or_404(Post, id=id)
    content = request.POST.get('content')
    Comment.objects.create(content=content, post=post)
    return redirect('posts:detail', post.id)

def delete(request, id):  # url 패턴의 /delete/<int:id>/ 의 id 값으로 데이터베이스 조회
    """ 게시글 삭제 View """
    context = {}
    post = Post.objects.get(id=id)  # Post 모델으 id 필드가 id인 데이터 조회
    if request.method == 'POST':
        post.delete()  # POST 요청인 경우 데이터 삭제
        return redirect('posts:list')  # url name list url로 리다이렉트 응답
    else:
        context.update(post=post)  # 10 줄에서 생성한 context 변수에 post 키로 post 값 업데이트
        return render(request, 'posts/confirm_delete.html', context)

def update(request, id):  # url 패턴의 /update/<int:id>/ 의 id 값으로 데이터베이스 조회
    context = {'title':'글 수정', 'submit_text': '수정하기'}  # form.html 사용 시 제목과 제출 버튼 이름 지정
    post = Post.objects.get(id=id)  # Post 모델으 id 필드가 id인 데이터 조회
    if request.method == 'POST':
        title = request.POST['title']  # form > input name이 title 값 가져오기
        content = request.POST['content']  # form > input name이 content 값 가져오기
        created_by = request.POST['created_by']  # form > input name이 created_by 값 가져오기
        
        post.title = title  # 21 줄에서 조회한 객체의 title 값 변경
        post.content = content  # 21 줄에서 조회한 객체의 content 값 변경
        post.created_by = created_by  # 21 줄에서 조회한 객체의 created_by 값 변경
        post.save()  # 데이터베이스에 반영(저장)
        return redirect('posts:detail', id)  # url 패턴 detial에 id값을 넣어 리다이렉트
    else:
        context.update(post=post)  # form에 기존 값 추가를 위해 21에서 조회한 Post 인스턴스 context에 업데이트
        return render(request, 'posts/form.html', context)
        
        

def list(request):
    post_all = Post.objects.all()  # Post 모델의 전체 데이터 조회 
    context = {'post_all': post_all}  # 응답의 context 데이터 생성
    return render(request, 'posts/list.html', context)  # 요청에 응답 함수, 'list.html'은 파일명이며 templates 폴더에 존재해야 함

def detail(request, id):
    post = Post.objects.get(id=id)  # Post 모델의 특정 데이터 조회
    comment_list = Comment.objects.filter(post=post)  # Comment 모델의 post필드가 위에서 조회한 post인 것 조회
    scrap = Scrap.objects.filter(user=request.user, post=post)
    context = {'post': post, 'comment_list': comment_list, 'scrap': scrap}
    return render(request, 'posts/detail.html', context)

# def new(request):
#         context = {'title':'글 등록', 'submit_text': '등록하기'}
#         return render(request, 'form.html', context)
    
def create(request):
    if request.method == 'POST':
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
        return redirect('home')
    else:
        context = {'title':'글 등록', 'submit_text': '등록하기'}
        return render(request, 'posts/form.html', context)

