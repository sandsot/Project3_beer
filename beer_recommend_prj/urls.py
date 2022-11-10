"""beer_recommend_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include

def root(request):
    return HttpResponse("home/을 추가해 오늘 시간 비어: 맥주 추천 페이지로 이동해주세요")

urlpatterns = [
    path('', root),
    path('account/', include('account.urls')),  # blog.urls에 있는 주소 앞에 blog/를 한 번에 붙이자.
    path('search/', include('search.urls')),
    path('community/', include('community.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
