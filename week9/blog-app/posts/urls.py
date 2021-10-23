from django.urls import path

from posts.views import list, detail, create, update, delete, comment_create, scrap  # new

app_name = 'posts'

urlpatterns = [
    path('<int:id>/scrap/', scrap, name='scrap'),
    path('<int:id>/comment/create/', comment_create, name='comment_create'),
    path('<int:id>/update/', update, name='update'),
    path('<int:id>/delete/', delete, name='delete'),
    path('<int:id>/', detail, name='detail'),
    path('', list, name='list'),
    # path('new/', new, name='new'),
    path('create/', create, name='create'),
]
