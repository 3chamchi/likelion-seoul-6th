from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # 장고에서 제공하는 사용자 모델, 장고 인증과 연결
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout  # 장고에서 제공하는 로그인, 로그아웃 기능


def signup(request):
    """ 회원가입 View """
    if request.method == 'POST':
        # POST 요청일 경우 회원가입 기능 수행
        if request.POST['password1'] == request.POST['password2']:  # 클라이언트 회원가입 시 비밀번호1, 2 동일한지 비교
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            # auth_login(request, user)
            return redirect('accounts:login')
    else:
        # GET 요청일 경우 회원가입 HTML 응답
        return render(request, 'accounts/signup.html')

def login(request):
    """ 로그인 View """
    if request.method == 'POST':
        # POST 요청일 경우 로그인 기능 수행
        username = request.POST['username']  # 클라이언트에서 form > input name이 username인 값 가져오기
        password = request.POST['password']  # 클라이언트에서 form > input name이 username인 값 가져오기
        user = authenticate(request, username=username, password=password)  # 장고에서 제공하는 사옹자 확인 함수 / 있는 경우 User 반환, 없는 경우 None 반환
        if user is not None:  # User가 None이 아닌 경우
            auth_login(request, user)  # 장고에서 제공하는 로그인 처리 함수
            return redirect('home')  # 다른 URL 경로 응답, URL name 사용 가능
        else:
            context = {'error': '아이디 또는 비밀번호가 잘못되었습니다.'}  # Template에서 사용할 데이터 정의
            return render(request, 'accounts/login.html', context)
    else:
        # GET 요청일 경우 로그인 HTML 응답
        return render(request, 'accounts/login.html')

def logout(request):
    """ 로그아웃 View """
    auth_logout(request)  # 로그아웃 처리
    return redirect('home')