from django.contrib import admin
from django.urls import path

from calculator.views import index as calculator_index
from lotto.views import index as lotto_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', calculator_index),
    path('lotto/', lotto_index),
]
