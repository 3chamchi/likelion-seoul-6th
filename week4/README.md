Django(2) - 첫 앱 만들기
---  
## 목차
[가상환경 생성 ~ 장고 개발서버 실행 순서](#가상환경-생성-~-장고-개발서버-실행-순서)  
[터미널 기록](#터미널-기록) 
 * [1. 가상환경 생성](#1-가상환경-생성) 
 * [2. 가상환경 접속](#2-가상환경-접속) 
 * [3. pip 업데이트](#3-pip-업데이트) 
 * [4. 장고 프로젝트 생성](#4-장고-프로젝트-생성) 
 * [5. 장고 개발서버 실행](#5-장고-개발서버-실행) 

## 터미널 내용 기록 파일
> 9월 4일 강의 터미널 내용을 정리한 파일입니다.

## 가상환경 생성 ~ 장고 개발서버 실행 순서
1. 가상환경 생성
2. 가상환경 접속
3. pip 업데이트
4. 장고 설치
5. 장고 개발 서버 실행  
  
## 터미널 기록
### 1. 가상환경 생성
* 경로 확인 : ``` /Users/won/Project/study/lieklion-seoul-6th/week4 ```
  * 명령어 : 윈도우 cd , 맥 pwd
```
# input : pwd 
# output : /Users/won/Project/study/lieklion-seoul-6th/week4

# Windows
python -m venv venv

# Mac os
python3 -m venv venv
```

### 2. 가상환경 접속
* 경로 확인 : ``` /Users/won/Project/study/lieklion-seoul-6th/week4 ```
* 현재 파일 확인 : ``` venv ```
  * 명령어 : 윈도우 dir 맥 ls
* 가상환경 접속
  * 
```
# input : pwd 
# output : /Users/won/Project/study/lieklion-seoul-6th/week4

# dir ls
# output : venv

# Windows
.\venv\Scripts\activate

# Mac os
source venv/bin/acticate
```
* 가상환경 접속 후 가상환경 접속 ``` (venv) ``` 필수 확인
  * ``` (venv) /Users/won/Project/study/lieklion-seoul-6th/week4```  

### 3. pip 업데이트
> 터미널의 ``` (venv) ``` 가상환경 접속이 된 것을 필히 확인
* pip 업데이트
```
# Windows
pip install --upgrade pip

# Mac os
pip3 install --upgrade pip
```

### 4. 장고 프로젝트 생성
* 생성 전 확인 사항 3가지
```
# 1) 현재 위치 확인
# input : pwd
# ouput : /Users/won/Project/study/lieklion-seoul-6th/week4

# 2) 가상 환경 접속 확인
# 터미널의 (venv) 확인

# 3) 현재 디렉토리 파일 확인
# input : Windows cd , Mac os ls
# output : venv
```
* 장고 프로젝트 생성 : ``` django-admin startproject config . ```

### 5. 장고 개발서버 실행
* 현재 디렉토리 확인
```
# 1) 현재 디렉토리 파일 확인
# input : Windows cd , Mac os ls
# output : config manage.py venv
```
* 개발서버 실행 : ``` python manage.py runserver ```
```
# input : python manage.py runserver

# output : Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 04, 2021 - 13:04:07
Django version 3.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
