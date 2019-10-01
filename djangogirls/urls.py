"""djangogirls URL Configuration


"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('blog.urls')),
    path('detail/', include('blog.urls'), name = 'detail'),
    url(r'^$', include('blog.urls')),
    path('', include('blog.urls'))
]
