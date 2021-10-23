from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from posts.views import list

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', list, name='home'),  # 메인 페이지 지정

    path('accounts/', include('accounts.urls')),  # accounts 앱의 urls 사용
    path('posts/', include('posts.urls')),  # posts 앱의 urls 사용
    path('scraps/', include('scraps.urls')),
    path('photolog/', include('photolog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
