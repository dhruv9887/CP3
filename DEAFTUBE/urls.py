"""
URL configuration for DEAFTUBE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from deaf import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path('videos',views.videos,name="videos"),
    path('channel',views.channel,name='channel'),
    path('login',views.login,name='login'),
    path('upload',views.upload,name='upload'),
    path('signup',views.signup,name='signup'),
    path('popup',views.popup,name='popup'),
    path('profile',views.profile,name='profile')
    ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,DOCUMENT_ROOT=settings.MEDIA_ROOT)
