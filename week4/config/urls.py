from django.contrib import admin
from django.urls import path

from lotto.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', index)
]
