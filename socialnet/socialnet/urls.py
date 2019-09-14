"""socialnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup1),
    path('login/', login1),
    path('homepage/',homepage),
    path('dp/',dp),
    path('error/',error),
    path('addpost/',addpost),
    path('viewpost/<int:id>',viewpost),
    path('like/<int:id>/',like1),
    path('comment/<int:id>/',comment1),
    path('addfriend/',addfriend),
    path('acceptrequest/',acceptrequest),
    path('cancelrequest/',cancelrequest),
    path('requestsent/',requestsent),
    path('showfriend/',showfriend),
    path('chatting/',chatting),
    path('logout/',logout),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
