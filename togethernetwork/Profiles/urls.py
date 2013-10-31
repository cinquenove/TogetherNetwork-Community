# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<profile_pk>\d+)$', views.profile_view, name='profile_view'),
    url(r'^edit$', views.edit_profile_view, name='edit_profile_view'),
)





