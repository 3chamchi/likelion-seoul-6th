from random import sample
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# https://docs.djangoproject.com/en/3.2/topics/templates/#django.template.backends.base.Template.render


def index(req):
    number_list = sample(range(1,46), 6)
    template = loader.get_template('index.html')
    context = {
        'number_list': number_list,
    }
    return HttpResponse(template.render(context))
