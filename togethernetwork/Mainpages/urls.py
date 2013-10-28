# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^about', views.about_view, name='about_view'), 
    url(r'^', views.homepage_view, name='homepage_view'), 
)




