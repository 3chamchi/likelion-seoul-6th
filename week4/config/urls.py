from django.contrib import admin
from django.urls import path

from lotto.views import index as lotto_index
from calculator.views import index as calculator_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto_index),
    path('calculator/', calculator_index),
    path('', calculator_index)
]
