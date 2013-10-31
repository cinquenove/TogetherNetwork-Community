# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<profile_pk>\d+)$', views.profile_view, name='profile_view'),
    url(r'^nobody$', views.profile_view, name='profile_view'),
)





