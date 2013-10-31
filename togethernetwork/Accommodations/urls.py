# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('', 
    url(r'^list', views.accommodations_view, name='accommodations_view'), 
    url(r'^$', views.accommodations_view, name='accommodations_view'), 
)




