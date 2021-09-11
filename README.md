멋쟁이사자처럼 직장인 서울 6기
=====
## HACK YOUR LIFE
### 당신의 아이디어를 실현해보세요.  

| 궁금하거나 질문은 언제든 슬랙을 통해 물어봐주세요!  
<br/>

## 목차
[Python](#python)  
- [공식문서](#공식문서)  
- [파이썬 명령어](#파이썬-명령어)  
- [알아두면 좋은 정보](#알아두면-좋은-정보)  
  - [용어](#용어)
  - [유용한 내장 함수](#유용한-내장-함수)
  - [자료형 및 연산자](#자료형-및-연산자)
  - [PEP8](#pep8)  

[장고](#장고)
- [공식문서](#공식문서)
- [장고 명령어](#장고-명령어)

[VSCode, 코드편집기](#vscode-코드편집기)  
- [단축키](#단축키)  
- [필수 확장 프로그램](#필수-확장-프로그램)  
- [추천 확장 프로그램](#추천-확장-프로그램)  
- [HTML, CSS 추천 확장 프로그램](#html-css-추천-확장-프로그램)  


# Python

## 공식문서
* [파이썬 공식 홈페이지 바로가기](https://www.python.org/)  
* [파이썬 공식문서 바로가기](https://docs.python.org/3/)  
* [파이썬 언어 레퍼런스 바로가기](https://docs.python.org/ko/3/reference/index.html)  
* [파이썬 용어집](https://docs.python.org/ko/3/glossary.html#glossary)

## 파이썬 명령어
> 맥북을 사용하시는 분은 ```python```을 ```python3```로 ```pip```를 ```pip3```로 사용하셔야합니다. 맥북엔 기본으로 사용하는 python이 있어 그렇습니다.  
### 패키지 확인
```
pip list
```  

### 패키지 설치
```
pip install 패키지명
```  

### 패키지 삭제
```
pip uninstall 패키지명
```  

### 패키지 업데이트
```
pip install --upgrade 패키지명
```

### 가상환경 생성
```
python -m venv 가상환경명
```

## 알아두면 좋은 정보
### 용어
* 뮤터블(mutable) : 변경 가능한
* 이뮤터블(Immutable) : 변경 불가능한
* 괄호 : 대괄호 [], 중괄호 {}, 소괄호 ()
* 들여쓰기(indent) : 들여쓰기, 탭(tab)보다 스페이스 4번 사용 권장

### 유용한 내장 함수
* ```id()``` : 객체의 《아이덴티티》를 돌려준다.
* ```type()``` : 인자 하나의 경우, object 의 형을 돌려줍니다.
* ```print()``` : objects 를 텍스트 스트림 file 로 인쇄하는데, sep 로 구분되고 end 를 뒤에 붙입니다. 있다면, sep, end, file 및 flush 는 반드시 키워드 인자로 제공해야 합니다.
* ```input()``` : prompt 인자가 있으면, 끝에 개행 문자를 붙이지 않고 표준 출력에 씁니다.

### 자료형 및 연산자
* [공식문서 바로가기](https://docs.python.org/ko/3/library/stdtypes.html)  

### PEP8
* Python 코드용 스타일 가이드
* [공식문서 바로가기](https://www.python.org/dev/peps/pep-0008/)
<br/><br/>  

### 파이썬 설치시 "Add python x.x to path"를 안한 경우
* 직접 파이썬 환경 변수를 설정해주어야 한다.<br/> 시스템에서 파이썬이 어디에 설치되었는지 알려주기 위함
* 윈도우 키 > 시스템 환경변수 > 환경 변수 > user에 대한 사용자 변수 > 변수 Path 편집 > 파이썬 설치 위치, Scripts 추가
  > 시스템 속성 > 고급 > 환경 변수 > user에 대한 사용자 변수 > 변수 Path 편집 > 파이썬 설치 위치, Scripts 추가
* 환경 변수
   * C:\Users\User\AppData\Local\Programs\Python\Python37\Scripts\
   * C:\Users\User\AppData\Local\Programs\Python\Python37\
# 장고
## 공식문서  
* [장고 공식 홈페이지 바로가기](https://www.djangoproject.com/)  
* [장고 공식문서 바로가기](https://docs.djangoproject.com/en/3.2/)  

## 장고 명령어
### 장고 설치
```
pip install django
```  

### 장고 프로젝트 생성
```
django-admin startproject 프로젝트명 프로젝트경로
```
> 디렉토리를 서비스명으로 만든 뒤 생상된 디렉토리에서 프로젝트명을 config로 만드는 것을 권장함
### 장고 앱 생성
```
django-admin startpapp 앱명
```

### 장고 개발서버 실행
```
python manage.py runserver
```
> 서버 실행 명력어 입력 시 manage.py 파일의 경로에 있어야 함
<br/><br/>

# VSCode, 코드편집기
## 단축키
* ```Ctrl``` + ```/``` : 주석, 코드 여러줄 가능
* ```Ctrl``` + ```K``` + ```F``` : 코드 자동 정렬 -> ```pip install autopep8``` 필요
* ```Ctrl``` + ```F``` : 활성 파일 내 단어 검색
* ```Ctrl``` + ``` ` ``` : 터미널 실행


## 기본 설정
### 기본 터미널 설정
* 명령 팔레트(```Ctrl``` + ```Shift``` + ```P```) > ```Terminal: Select Default Profile``` > ```cmd``` 선택

## 필수 확장 프로그램
> VSCode 확장 프로그램이란 VSCode의 기본기능의 외에 기능을 추가하는 것으로 사용자에게 도움을 주는 추가 프로그램  
### python 
* 파이썬 개발의 필수로 파이썬 개발을 도와줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### python snippets 
* 파이썬 자동완성 서포트
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=frhtylcn.pythonsnippets)

### django 
* 장고 템플릿 언어 지원
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)

### SQLite
* 개발 테스트용 SQLite 뷰어 지원
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
<br/><br/>  

## 추천 확장 프로그램  
### Better Comments 
* 주석의 활용(기능)을 높여줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)

### Python Docstring Generator 
* 함수의 주석 생성을 도와줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

### indent-rainbow 
* 들여쓰기를 색상으로 구분해줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)

### Bracket Pair Colorizer 
* 괄로를 생상으로 구분할 수 있게 도와줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)

## HTML, CSS 추천 확장 프로그램
### Live Server 
* HTML, CSS 수정 시 브라우저에 즉시 반영
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

### Auto rename tag
* HTML 태그 수정이 여는태그, 닫는 태그를 동시에 변경해줍니다.
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)

### HTML CSS Support 
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css)

### CSS Peek
* [다운로드 링크](https://marketplace.visualstudio.com/items?itemName=pranaygp.vscode-css-peek)