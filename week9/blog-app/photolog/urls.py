
from django.urls import path

from .views import list, create

app_name = 'photolog'

urlpatterns = [
	path('', list, name='list'),
	path('create/', create, name='create'),
]
