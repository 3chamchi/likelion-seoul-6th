from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from posts.models import Scrap

@login_required
def list(reqeust):
    scrap_list = Scrap.objects.filter(user=reqeust.user)
    context = {'scrap_list':scrap_list}
    return render(reqeust, 'scraps/list.html', context)