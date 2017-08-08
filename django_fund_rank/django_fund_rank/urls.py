"""django_fund_rank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin
from fund_rank import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #这里使用的正则表达式进行url的匹配
    url(r'^$', views.index),
    url(r'^getStudentInfo$', views.getStudentInfo),# Notice this line
    url(r'^getFundRankList$', views.getFundRankList),# Notice this line

]
