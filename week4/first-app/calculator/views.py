from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # 1.사용자에게 값을 받는다.
    # text = request.GET['text']
    text = request.GET.get('text')
    print(text)

    # 2.값이 존재할 경우 계산을 한다.
    if text:
        result = eval(text)
        print(result)
    else:
        result = None

    # 3.응답을 한다
    return render(request, 'index.html', {'result':result})
    # return HttpResponse('index()...' + str(result))