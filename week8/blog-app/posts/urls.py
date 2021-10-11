from django.urls import path

from posts.views import list, detail, create, update, delete  # new

app_name = 'posts'

urlpatterns = [
    path('<int:id>/update/', update, name='update'),
    path('<int:id>/delete/', delete, name='delete'),
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    # path('new/', new, name='new'),
    path('create/', create, name='create'),
]
