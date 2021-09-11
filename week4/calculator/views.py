from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    formula = request.GET.get('formula')
    print(formula)
    
    result = None
    if formula:
        result = eval(formula)
    else: 
        result = None

    return render(request, 'calculator.html', {'result': result})
    # http_result = 'HttpResponse()'+ str(result)
    # return HttpResponse(http_result)