import random

from django.shortcuts import render


def index(request):
    lotto_number = random.sample(range(1, 46), 7)
    context = {
        'lotto_number': lotto_number,
    }
    return render(request, 'lotto.html', context)
