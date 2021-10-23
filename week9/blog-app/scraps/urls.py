from django.urls import path
from .views import list

app_name = 'scraps'

urlpatterns = [
	path('', list, name='list'),
]
