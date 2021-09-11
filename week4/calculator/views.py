from django.shortcuts import render  # HttpResponse 클래스를 응답하나 Tempalte 응답을 위한 코드가 포함된 함수
from django.http import HttpResponse  # 기본 적인 요청의 응답 클래스 임포트

# Create your views here.
def index(request):
    """ 계산기 요청을 처리할 함수 """
    formula = request.GET.get('formula')  # 쿼리스트링을 통해 수신한 값을 formula 변수 할당, 'reqeust.GET'은 딕셔너리 자료형이며 값이 없는 경우 None을 주기 위해 .get() 함수 사용
    print(formula)  # 값이 잘들어왔는지 터미널에 출력해보기 위한 코드
    
    result = None  # 코드라인 10, 14번째 중 1개의 코드라인만 사용 가능, result 코드라인 16번째에 result 값이 없는 경우를 대비한 변수 생성
    if formula:  # 클라이언트로 부터 formula 값을 받은 경우 계산 기능 실행
        result = eval(formula)  # eval() 파이썬 내장 함수로 문자열로 들어오는 수식을 계산하여 결과값을 반환함
    else: 
        result = None

    return render(request, 'calculator.html', {'result': result})  # render() 함수는 Template 응답을 위해 사용되며 HttpResponse() 클래스 응답을 포함하고 있음
    # http_result = 'HttpResponse()'+ str(result)  # Template 없이 응답
    # return HttpResponse(http_result)  # Template 없이 응답