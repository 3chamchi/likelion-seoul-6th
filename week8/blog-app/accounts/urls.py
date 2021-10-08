from django.urls import path
from .views import signup, login, logout

app_name = 'test'

urlpatterns = [
		path('signup/', signup, name='signup'),
		path('login/', login, name='login'),
		path('logout/', logout, name='logout'),
]
